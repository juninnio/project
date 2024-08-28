Brain Tumor Segmentation using 3D MRI Images. [Project in Progress]

Description
----------------
Project is based on BraTS2021 Challenge Task 1. Project task is to segment brain tumor to 3 classes: 
- Tumor Core
- Enhancing Tumor
- Whole tumor

Dataset Description
------------------------
Dataset is obtained from Kaggle: [https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1](url)
Dataset contains 1000+ patients' 3D MRI Images with 4 different modalities and corresponding segmentation mask.
There are 3 different segmentation as mentioned above, but there are 4 ground truth labels in each segmentation mask :
0 : Background
1 : Necrotic and non-enhancing tumor core
2 : Peritumoral Edema
4 : Enhancing Tumor
Each MRI Image are in (240,240,155) dimension

Methods
-----------
1. Loading the Data
Nibabel library is used to load the data. However, as the size of the whole data is too big to load at once in my local machine and google colab (16 Gb of RAM), Custom 3D Generator is built.
Generator is used to generate batches of data on-the-fly and feeding it to model to prevent memory overconsumption. Furthermore, Data Augmentation is also done in the generator to further reduce memory consumption.

2. Model
The model chosen is Residual Attention 3D U-Net. This model is based on these papers:
- https://arxiv.org/pdf/1804.03999v3
- https://link.springer.com/chapter/10.1007/978-3-030-72084-1_30 [p.183, Brain Tumor Segmentation using Dual-Path Attention 3D U-Net in 3D MRI Images, Wen Jun, Xu Haoxiang, and Zhang Wang]

The performance is not yet known as this project is still in progress.
