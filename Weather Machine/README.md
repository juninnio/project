Project : Weather Machine

Description : This project is about predicting next day's chance of rain.

Equipment: Raspberry Pi with weather sensors.

Technologies used:
- Data Storage : Amazon AWS S3 Bucket & Amazon AWS RDS.
- Machine Learning : Tensorflow (Neural Network and model & weights dumping), sci-kit learn, pandas (dataset manipulation), pickle (objects dumping).
- Visualization : Matplotlib & seaborn
- File manipulation and others : time, datetime, mysql, shutil

Mechanism :
This project consists of 2 main files for coding:
1. weather_ml.ipynb : contains code for data preprocessing, feature engineering, and machine learning model.
2. running_script.py : contains code for fetching, processing, making predictions, and uploading data.

Model Building:
1. Started by using australian weather dataset as weather is extremely unpredictable and inconsistent in countries around the world, for this project WeatherAUS2.csv is used. (Dataset is obtained via Kaggle)
2. Perform data preprocessing which includes but not limited to scaling the dataset, encoding categorical variable, performing value mapping for categorical variable, feature engineering, etc.
3. Testing and building various machine learning algorithm. SVM, KNN, Decision Tree, Random Forest, Naive Bayes, Logistic Regression, and Artificial Neural Network were tested.
   - The results were similar and in the range of 75-87% and Artificial Neural Network provided the highest accuracy, which is later used and other models were deleted.
4. To save time of retraining the model every single time, the model and weights are saved into local machine (dumped). Using tensorflow library, the model is saved in json format, while the weights are saved in h5 format. It is important to have the same weights as the model performance will definitely be different with different weights.
5. Encoder and Scaler are also saved (dumped) using pickle library with the same reason as the weights.
6. These saved model and preprocessing steps are later used in another python script to automate the process of quering data, preprocessing and making prediction, and uploading the informations and prediction to MySQL database in AWS RDS.

System:
1. Raspberry Pi and weather sensors collects data and sends it to Amazon AWS S3 Bucket.
- running_script.py:
2. Fetch one-day data and downloads it to a folder. Before downloading, the code deletes the folder and recreate it. (This is not the best system as Amazon Sagemaker can be utilized, but for some reason, my Sagemaker wasn't working.)
3. Preprocess data and features to match trained model's attributes. Scaler and encoder dumped from weather_ml.ipynb (le1.pkl and sc1.pkl) are used to get consistent results.
4. Get dumped model and weights from weather_ml.ipynb (model.json and model.weights.h5) and input the preprocesssed data and features into the model to make predictions.
5. Unprocessed data & prediction are uploaded to Amazon RDS where the record is then queried by web dashboard (made by my groupmates) to show the informations.

This process refresh every one minute to ensure the latest information. Another consideration in this project is as data is uploaded every minute by raspberry pi, it would be to much to download at one point, so we fecth latest data in 10 minute intervals.
