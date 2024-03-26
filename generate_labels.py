import csv
import numpy as np

def diagnose(array):
    if array[0] == '1':
        return "NORMAL"
    if array[1] == '1':
        return "ACTIONABLE"
    if array[2] == '1':
        return "BENIGN"
    return "CANCER"

file_paths = r'Validation\BCS-DBT-labels-validation-PHASE-2-Jan-2024.csv'
with open(file_paths, 'r') as f:
    paths = f.readlines()[1:]

paths = [line.strip().split(",") for line in paths]
paths = np.array(paths)

validation_labels = 'validation_labels.txt'
with open(validation_labels, 'w') as w:
    for line in paths:
        status = diagnose(line[-4:])
        w.write(",".join((line[0], line[2], status)) + '\n')
