import numpy as np
import matplotlib.pyplot as plt
# from duke_dbt_data import dcmread_image, read_boxes, draw_box

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


file_path = 'Validation\Validation NPY\DBT-P00431,rmlo.npy'
with open(file_path, 'rb') as f:
    data = np.load(f)

# plt.imshow(data[27,:,:], cmap='gray')
# plt.show()
# print(data.shape)
# print(data.dtype)
# print(np.max(data))
# print(np.min(data))
    
image = draw_box(data[27,:,:], x=1418, y=651, width=212, height=201, lw=10)
plt.imshow(image, cmap=plt.cm.gray)
plt.show()