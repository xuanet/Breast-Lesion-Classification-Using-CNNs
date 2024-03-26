import numpy as np
import matplotlib.pyplot as plt

file_path = 'Validation\Validation NPYDBT-P00002,lcc.npy'
with open(file_path, 'rb') as f:
    data = np.load(f)

plt.imshow(data[45,:,:])
plt.show()
print(data.shape)
print(data.dtype)
print(np.max(data))
print(np.min(data))