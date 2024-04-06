import numpy as np
import os
import extract_slice_utils as esu

DEBUG = False
IGNORE = [['DBT-P01150', 'lmlo'], ['DBT-P03027', 'lcc'], ['DBT-P03027', 'lmlo']]

box_path = 'Validation\BCS-DBT-boxes-validation-v2-PHASE-2-Jan-2024.csv'
npy_path = 'Validation\Validation NPY'
save_path = 'Validation\Validation Boxes'

valid, boxes_name, boxes_slice, directory = esu.length_check(box_path, npy_path)
if (valid is False):
    print('error parsing')



else:
    print('length expected')
    esu.create_slices(save_path, npy_path, boxes_name, boxes_slice, directory, DEBUG, IGNORE)

