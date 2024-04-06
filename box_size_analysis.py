import numpy as np
import matplotlib.pyplot as plt

file_path = 'Test\BCS-DBT-boxes-test-v2-PHASE-2-Jan-2024.csv'


with open(file_path, 'r') as f:
    paths = f.readlines()[1:]

paths = [line.strip().split(',') for line in paths]
paths = np.array(paths)
# paths[:, 7:9] = paths[:, 7:9].astype(int)

# column 7, 8 are width, height

# print(paths[:, 7:9].astype(int))

# width = np.histogram(paths[:, 7].astype(int))
# height = np.histogram(paths[:, 8].astype(int))

print('mean_width', np.mean(paths[:,7].astype(int)))
print('mean_height', np.mean(paths[:,8].astype(int)))

fig, ax = plt.subplots(1, 2)
ax[0].hist(paths[:, 7].astype(int), bins='auto')  # arguments are passed to np.histogram
ax[0].set_title('width')
ax[1].hist(paths[:, 8].astype(int), bins='auto')  # arguments are passed to np.histogram
ax[1].set_title('height')
plt.show()



