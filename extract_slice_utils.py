import numpy as np
import matplotlib.pyplot as plt
import os

def draw_box(
    image: np.ndarray,
    x: int,
    y: int,
    width: int,
    height: int,
    color = None,
    lw=10,
):
    """Draw bounding box on the image"""
    x = min(max(x, 0), image.shape[1] - 1)
    y = min(max(y, 0), image.shape[0] - 1)
    if color is None:
        color = np.max(image)
    if len(image.shape) > 2 and not hasattr(color, "__len__"):
        color = (color,) + (0,) * (image.shape[-1] - 1)
    image[y : y + lw, x : x + width] = color
    image[y + height - lw : y + height, x : x + width] = color
    image[y : y + height, x : x + lw] = color
    image[y : y + height, x + width - lw : x + width] = color
    return image

def display(slice):
    plt.imshow(slice, cmap='gray')
    plt.show()


def get_clicked_coordinates(slice):
    def onclick(event):
        plt.close()
        x = int(event.xdata)
        y = int(event.ydata)
        get_clicked_coordinates.clicked_coordinates = (x, y)

    fig = plt.figure()
    plt.imshow(slice, cmap='gray')
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    
    return get_clicked_coordinates.clicked_coordinates

def length_check(box_path, npy_path):

    with open(box_path, 'r') as f:
        boxes = f.readlines()[1:]

    boxes = [line.strip().split(',') for line in boxes]
    boxes_name = [[line[0], line[2]] for line in boxes]
    # Slice, X, Y, width, height
    boxes_slice = [[line[0], line[2], int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8])] for line in boxes]

    counter = 0
    directory = os.fsencode(npy_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        name = filename[:-4].split(",")
        if name in boxes_name:
            counter += boxes_name.count(name)
            if boxes_name.count(name) > 1:
                print(boxes_name.count(name))
                print(name)

    print(f'expected {len(boxes)}, got {counter}')


    return True if counter == len(boxes) else False, boxes_name, boxes_slice, directory
    
def create_slices(save_path, npy_path, boxes_name, boxes_slice, directory, DEBUG, IGNORE):
    normal_count = 0
    predefined_count = 0
    ignored_count = 0
    for file in os.listdir(directory):
        # iterate over files in NPY directory
        filename = os.fsdecode(file)
        name = filename[:-4].split(",")
        img_path = os.path.join(npy_path, filename)
        if name in boxes_name:
            if name in IGNORE:
                print(f'faulty data: {filename}')
                ignored_count += 1
                predefined_count += 1
                continue
            print(f'predefined box: {filename}')
            index = boxes_name.index(name)
            params = boxes_slice[index]
            with open(img_path, 'rb') as f:
                data = np.load(f)
            if DEBUG:
                slice = draw_box(data[params[2]], params[3], params[4], params[5], params[6])
                display(slice)
            else:
                complete_save_path = os.path.join(save_path, filename)
                with open(complete_save_path, 'wb') as s:
                    area = data[params[2], params[4]:params[4]+params[6], params[3]:params[3]+params[5]]
                    np.save(s, area)  

            predefined_count += 1 
        else:
            print(f'user input: {filename}')
            normal_count += 1
            print(f'normal count: {normal_count}')
            if not DEBUG and normal_count < 201:
                with open(img_path, 'rb') as f:
                    data = np.load(f)
                middle_slice = data.shape[0]//2
                complete_save_path = os.path.join(save_path, filename)
                with open(complete_save_path, 'wb') as s:
                    x, y = get_clicked_coordinates(data[middle_slice])
                    print(x, y)
                    area = data[middle_slice, y:y+225, x:x+225]
                    np.save(s, area)

    if predefined_count != len(boxes_name):
        print(f'error with predefined boxes, expected {len(boxes_name)} but got {predefined_count}')
    print(f'ignored count: {ignored_count}')

                


