Brain Tumor Segmentation using 3D MRI Images.
To clone : [https://github.com/juninnio/Brain-Tumor-Segmentation-unet](url)

Description
----------------
Project is based on BraTS2021 Challenge Task 1. Project task is to segment brain tumor to 3 classes: <br>
- Tumor Core
- Enhancing Tumor
- Whole tumor

Dataset Description
------------------------
Dataset is obtained from Kaggle: [https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1](url)<br>
Dataset contains 1000+ patients' 3D MRI Images with 4 different modalities and corresponding segmentation mask.<br>
There are 3 different segmentation as mentioned above, but there are 4 ground truth labels in each segmentation mask :<br>
0 : Background<br>
1 : Necrotic and non-enhancing tumor core<br>
2 : Peritumoral Edema<br>
3 : Enhancing Tumor (Converted into 3 from 4)<br>
Each MRI Image are in (240,240,155) dimension

Methods
-----------
1. Loading the Data<br>
The dataset consist of 1250+ 3D images in nii.gz format. For this type of file, Nibabel library is used to load the images and get the data.
Due to several resource costraint, the data is loaded into a custom generator data loading pipeline. There are 2 version of this data pipeline:<br>
  i. The custom generator accepts file path and preprocess the data on-the-fly before feeding it to model in batches.<br>
  ii. Custom data pipeline accepts file path and preprocess the data before saving it into numpy file. Then the custom generator accepts the file path of numpy file and load it as np file in batches and feed it to the model.<br>

The preprocessing steps:<br>
  i. Cropping the images into (128,128,128) patches and stacking 3 of the modalities (t1ce, t2, and flair). The reason t1 is not used is as t1ce is already available which is contrast enhanced version of t1. <br>
  ii. Normalizing the images using MinMaxScaler from scikit-learn library. <br>
  iii. Seperting each class in 3D segmentation images and stacking it into 4 channels. <br>

After preprocessing, the shape of each image will be (128,128,128,3) while the segmentation mask will be (128,128,128,4).

2. Model<br>
The model chosen is Residual Attention 3D U-Net. This model is based on these papers:
- https://arxiv.org/pdf/1804.03999v3
- https://link.springer.com/chapter/10.1007/978-3-030-72084-1_30 [p.183, Brain Tumor Segmentation using Dual-Path Attention 3D U-Net in 3D MRI Images, Wen Jun, Xu Haoxiang, and Zhang Wang]

The model leverage the attention block to focus the CNN attention to important features and the residual block to allow CNN to remember a lower dimension feature.

3. Output<br>
The prediction/output of this project as well as the metrics is explained in the python notebook itself.

Notes 
------------
checkpoints are used as this model was trained in google colab and there are bugs in google colab which causes the session to disconnect after a while.<br>
This model was trained for 20 epoch in 8 hours before the session disconnects and the final model was saved.<br>
The prediction outputted in the notebook was the result of 20 epochs of training, which lead to the belief that this model can be improved with more training.<br>
The saved model is also included in this directory to support those who wants to experiment using this project. <br>
All the codes are my personal work with the help of my teacher and a bit of chatGPT.<br>
<br>
For any questions, please contact me on LinkedIn.
