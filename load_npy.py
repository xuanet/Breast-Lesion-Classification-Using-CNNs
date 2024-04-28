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
    lw=4,
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

def load_single_image(image_path, d3=False, slice=0):
    with open(image_path, 'rb') as f:
        data = np.load(f)
    if d3:
        data = data[slice]
    plt.imshow(data, cmap=plt.cm.gray)
    plt.show()


def load_directory(folder_path):
    directory = os.fsencode(folder_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        image_path = os.path.join(folder_path, filename)
        load_single_image(image_path)
    

# load_directory('Train\Training Boxes')
load_single_image('Train\Training Boxes\DBT-P01302,rcc.npy')

