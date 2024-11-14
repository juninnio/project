Brain MRI Classification using ResNet34 with Grad-CAM Visualization
----------------------------------------------------------------------

This project is focused on training a ResNet34 model to classify brain MRI images, providing Grad-CAM visualizations for interpretability. The model is designed with transfer learning techniques and image pre-processing methods to enhance feature detection and improve classification accuracy across multiple categories.

Project Structure
--------------------
- Data Loading and Preprocessing: Utilizes ImageDataGenerator to handle data augmentation and resizing. Training, validation, and test sets are dynamically created, and image standardization techniques are applied.
- Model Architecture: A ResNet34-based convolutional neural network with residual blocks for deeper feature extraction. Custom implementation of residual blocks and shortcut connections enables efficient feature mapping for the input data.
- Training and Evaluation: Model is trained on labeled brain MRI images, with training and validation accuracy tracked across epochs. The model's performance on the test set is evaluated post-training.
- Grad-CAM Visualization: Grad-CAM (Gradient-weighted Class Activation Mapping) is implemented to create heatmaps highlighting the regions the model focuses on while predicting classes. This is useful for model interpretability and understanding decision-making areas within the MRI scans.
- Image Processing and Renormalization: Image normalization and renormalization functions are created to standardize MRI images, center values, and avoid pixel overflow or underflow issues, essential for clearer and more reliable model predictions.

Results
------------------
The model achieves high classification accuracy on MRI scans, helping identify brain-related abnormalities. Grad-CAM visualizations aid in explaining model decisions by highlighting focused areas on MRI scans.