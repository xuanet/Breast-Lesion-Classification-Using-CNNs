import pydicom as dicom
import matplotlib.pylab as plt
import numpy as np
import os
# Validation\Validation Images\manifest-1617905855234\Breast-Cancer-Screening-DBT\DBT-P00001\01-01-2000-DBT-S00597-MAMMO SCREENING DIGITAL BILATERAL-78647\16214.000000-NA-18959\1-1.dcm
path_prefix = r"Validation\Validation Images\manifest-1617905855234"
file_paths = r'Validation\BCS-DBT-file-paths-validation-v2.csv'
save_path = r'Validation\Validation NPY'
with open(file_paths, 'r') as f:
    paths = f.readlines()[1:]

paths = [line.strip().split(",") for line in paths]
paths = np.array(paths)

total = len(paths)
iter = 0
for i in range(total):
    file_name = ",".join((paths[i][0], paths[i][2])) + '.npy'
    image_path = os.path.join(path_prefix, paths[i][3])
    image_path = image_path.replace('/', '\\')
    ds = dicom.dcmread(image_path)
    ds[0x0028, 0x0101].value = 16
    data = ds.pixel_array
    complete_save_path = os.path.join(save_path, file_name)
    with open(complete_save_path, 'wb') as s:
        np.save(s, data)
    iter += 1
    print(f"processed {iter} images")


