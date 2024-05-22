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

System:
1. Raspberry Pi and weather sensors collects data and sends it to Amazon AWS S3 Bucket.
- running_script.py:
2. Fetch one-day data and downloads it to a folder. Before downloading, the code deletes the folder and recreate it. (This is not the best system as Amazon Sagemaker can be utilized, but for some reason, my Sagemaker wasn't working.)
3. Preprocess data and features to match trained model's attributes. Scaler and encoder dumped from weather_ml.ipynb are used to get consistent results.
4. Get dumped model from weather_ml.ipynb and input the preprocesssed data and features into the model to make predictions.
5. Unprocessed data & prediction are uploaded to Amazon RDS where the record is then queried by web dashboard (made by my groupmates) to show the informations.

This process refresh every one minute to ensure the latest information. Another consideration in this project is as data is uploaded every minute by raspberry pi, it would be to much to download at one point, so we fecth latest data in 10 minute intervals.
