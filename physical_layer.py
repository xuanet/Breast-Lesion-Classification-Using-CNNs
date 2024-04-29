import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from skimage.transform import resize
from matplotlib.colors import Normalize

file_path = 'Validation\Validation Boxes\DBT-P00001,lmlo.npy'

with open(file_path, 'rb') as f:
    slice = np.load(f)
slice = slice / np.max(slice)
slice[slice < 0.01] = 0
slice = resize(slice, (225, 225))


# reduce resolution with conv
"""the size and number of detector elements, 
the size of the X-ray focal spot, and the
source-object-detector distances"""

lpf = np.ones(shape=(4, 4))
filtered_slice = sp.signal.convolve2d(slice, lpf, mode='same') / lpf.size


# reduce contrast with norm function
"""voltage (intensity), detector sensitivity"""

def low_contrast(image, degree):
    """gamma correction, gamma < 1 is less contrast"""
    # Apply gamma correction
    d = 1 + np.exp(-degree*(image-0.5))
    return 1 / d

low_contrast_slice = low_contrast(slice, 4)

# combine low res + low contrast

combined_slice = low_contrast(filtered_slice, 4)

# print(slice.dtype)
# print(filtered_slice.dtype)
# print(low_contrast_slice.dtype)
# print(combined_slice.dtype)

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# Plot each subplot with its own colormap
cmap = 'gray'
norm = Normalize(vmin=0, vmax=1)

im0 = ax[0][0].imshow(slice, cmap=cmap, norm=norm)
ax[0][0].set_title('original')

im1 = ax[0][1].imshow(filtered_slice, cmap=cmap, norm=norm)
ax[0][1].set_title('low res')

im2 = ax[1][0].imshow(low_contrast_slice, cmap=cmap, norm=norm)
ax[1][0].set_title('low contrast')

im3 = ax[1][1].imshow(combined_slice, cmap=cmap, norm=norm)
ax[1][1].set_title('low res + low contrast')

# Create colorbar axes
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])  # [left, bottom, width, height]

# Add colorbars to the colorbar axes
fig.colorbar(im0, cax=cbar_ax, orientation='vertical', label='Intensity')

# Adjust layout
fig.tight_layout()

# Show the plot
plt.show()