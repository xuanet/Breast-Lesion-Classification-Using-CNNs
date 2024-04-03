import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

file_path = 'Validation\Validation NPY\DBT-P00001,lcc.npy'

with open(file_path, 'rb') as f:
    data = np.load(f)
shape = data.shape
slice = data[shape[0]//2]
slice = slice / np.max(slice)

# reduce resolution with conv
"""the size and number of detector elements, 
the size of the X-ray focal spot, and the
source-object-detector distances"""

lpf = np.ones(shape=(20, 20))
filtered_slice = sp.signal.convolve2d(slice, lpf, mode='same')

# reduce contrast with norm function
"""voltage (intensity), detector sensitivity"""

def low_contrast(slice, gamma=1.0):
    """gamma correction, gamma < 1 is less contrast"""
    res = np.power(slice, gamma)
    res = (res - np.min(res)) / (np.max(res) - np.min(res))

    return res

low_contrast_slice = low_contrast(slice, gamma=0.5)

# combine low res + low contrast

combined_slice = low_contrast(filtered_slice, gamma=0.5)

# print(slice.dtype)
# print(filtered_slice.dtype)
# print(low_contrast_slice.dtype)
# print(combined_slice.dtype)

fig, ax = plt.subplots(2, 2)
ax[0][0].set_title('original')
ax[0][0].imshow(slice, cmap='gray')

ax[0][1].set_title('low res')
ax[0][1].imshow(filtered_slice, cmap='gray')

ax[1][0].set_title('low contrast')
ax[1][0].imshow(low_contrast_slice, cmap='gray')

ax[1][1].set_title('low res + low contrast')
ax[1][1].imshow(combined_slice, cmap='gray')
fig.tight_layout()
plt.show()