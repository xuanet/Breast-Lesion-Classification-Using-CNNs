# Breast Lesion Classification

## Introduction
We develop and evaluate 3 machine learning models in TensorFlow for classifying breast lesions (Normal/Actionable, Benign, Cancerous) based on convolutional neural networks. Data is given as digital breast tomosynthesis (DBT) images and is taken from https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/

## Pipeline
```process.py``` takes the compressed 3D dicom images and turns them into 3D numpy arrays. ```extract_slice.py``` and its helper module ```extract_slice_utils.py``` extracts the lesion-containing bounding box for benign and cancerous images or allows the user to select a bounding box containing healthy tissue for the normal/actionable images. ```generate_labels.py``` creates a list associating image names with their classification. ```PhysicalLayerTransform.ipynb``` applies physical layers (low resolution, low contrast, combined) to the bounding boxes. The functions used to apply the physical layers are replicated in ```physical_layer.py```, and a sample transformation can be seen in ```physical_layer.png```. In ```models.ipybn```, the 3 models are designed and evaluated on each set of data. 

## Analysis
Our models were trained on Google Colaboratory using its L4 GPU. The folder containing data and analysis can be found at https://drive.google.com/drive/folders/1NQN6uYiKDY77k_TGe4B4n8lH7meUDriM?usp=drive_link

## Further notes
We found that researchers mis-located some bounding boxes. Some mis-located images are listed in ```mislabels.txt```. During training, clearly mis-located images are omitted.



