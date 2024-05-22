#getting the files
import boto3
import os
import shutil
from tensorflow.keras.models import model_from_json
from pickle import load
import pandas as pd
import time
import mysql.connector
from datetime import datetime, timedelta

def download_file(bucket_name, prefix, local_dir): #changed
    acc_key = "" #change for s3 bucket acc key
    secret_key = "" #change for s3 bucket secret key
    session = boto3.Session(
        aws_access_key_id=acc_key,
        aws_secret_access_key=secret_key,
    )
    s3 = session.client('s3')

    res = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    all_files = (res.get('Contents',[]))

    for obj in range(len(all_files)-1,0,-10):
        local_file_path = os.path.join(local_dir,os.path.basename(all_files[obj]['Key']))
        s3.download_file(bucket_name, all_files[obj]['Key'], local_file_path)
        print(f'Downloaded file from AWS: {all_files[obj]["Key"]}')


def del_folder(dir): #deleting folder (just for convenience)
    try:
        shutil.rmtree(dir)
        print("Files deleted successfully")
    except OSError as e:
        print('nothing found')

def create_folder(folder_path): #creating the folder again
    try:
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except OSError as e:
        print(f"Error: {folder_path} - {e.strerror}")


#combining downloaded file into one csv
def combine_csv_files(folder_path):
    # List all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    csv_files = sorted(csv_files)

    # Initialize an empty list to store dataframes
    dfs = []

    # Read each CSV file and append its contents to the list of dataframes
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

    # Concatenate all dataframes into a single dataframe
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

#data preprocessing and machine learning phase
#load model, encoder, and scaler
def machine_learning(df):
    model_dir = f'{os.getcwd()}/Python/Project'
    json_file = open(f'{model_dir}/model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(f"{model_dir}/model.weights.h5")
    scaler = load(open(f'{model_dir}/sc1.pkl','rb')) #scaler
    encoder = load(open(f'{model_dir}/le1.pkl','rb')) #encoder

    sunshine = df['Light'].apply(lambda x:(1/6) if x >= 10 else 0) #change this by testing the amount of lux received in sunny day
    rain = df['Rainfall'].apply(lambda x: 1 if x > 0 else 0)
    df['Sunshine'] = sunshine
    df = df.drop('Light', axis=1)
    df['RainToday'] = rain
    df = df.rename(columns={'Wind': "WindSpeed"})
    df['Date'] = pd.to_datetime(df['Date'])
    old_df = df.iloc[-1:]


    #new df
    #Min Temp: min temperature
    min_temp = min(df['Temperature'])
    #Max Temp: max temperature
    max_temp = max(df['Temperature'])
    #Rain Today: max of rain today
    rain_today = max(df['RainToday'])
    #Temperature: avg
    temp = (df['Temperature'].sum()/len(df))
    #Humidity: avg
    hum = (df['Humidity'].sum()/len(df))
    #Pressure : avg
    press = (df['Pressure'].sum()/len(df))
    #Sunshine: sum
    suns = df['Sunshine'].sum()
    #wind: avg
    ws = df['WindSpeed'].sum()/len(df)
    #rainfall: sum
    rf = max(df['Rainfall'])
    #wind direction : mode
    winddir = df['Wind Direction'].mode()[0]
    ##v
    data = pd.DataFrame({
        'MinTemp': [min_temp],
        'MaxTemp': [max_temp],
        'Rainfall': [16.7],
        'Sunshine': [5],
        'RainToday': [1],
        'WindSpeed': [ws],
        'Temperature': [temp],
        'Humidity': [hum],
        'Pressure': [press],
        'Wind Direction': [winddir]
    })

    #mapping direction
    dir_map = {'East' : 'E',
            'South East': 'SE',
            'South' : 'S',
            'South West': 'SW',
            'West' : 'W',
            'North West':'NW',
            'North':'N',
            'North East':'NE'}
    data['Wind Direction'] = data['Wind Direction'].apply(lambda x: dir_map[x])

     #label encoding
    data['Wind Direction'] = encoder.transform(data['Wind Direction'])

    columns = ['MinTemp', 'MaxTemp','Rainfall','Sunshine','RainToday','WindSpeed','Temperature','Humidity','Pressure','Wind Direction']
    data = data[columns]
    #scaling
    nr = data.drop('RainToday', axis =1 )
    sc_cols = nr.columns
    data[sc_cols] = scaler.transform(data[sc_cols])

    #making prediction
    prediction = loaded_model(data)
    print(f"Predicted Chance of Rain tomorrow: {prediction[0][0]*100:.2f}%")
    #done dont change
    return old_df[["Date","Temperature", "Rainfall", "WindSpeed", "Humidity", "Pressure", "Wind Direction"]], (round(float(prediction[0][0])*100,2))


def db_up(pred, dataset):
    usr = ""
    pwd = ""
    try:
        # Connect to the RDS MySQL database
        db = mysql.connector.connect(
            host="mydatabase.cvu00ge8qbju.ap-southeast-2.rds.amazonaws.com",
            user=usr, #change username
            password=pwd, #change pwd
            database="mydatabase"
        )

    except mysql.connector.Error as err:
        # Print error message if connection fails
        return("Error:", err)

    cursor = db.cursor()
    val = list(dataset.values[0])
    val.append(pred)
    values = tuple(val[1:])
    script = f"INSERT INTO weather_data (Date, Temperature, Rainfall, Wind, Humidity, Pressure, Wind_Direction, Rain_Tomorrow) VALUES (CURDATE(),%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(script, values)
    db.commit()
    print(f"Inserted Readings and Prediction to MySQL Database in AWS")
    db.close()

def main():
    while True:
        today = (datetime.now()).strftime("%d-%m-%Y")
        custom_time = "11-05"
        bucket_name = 'goofygooberweatherstation'
        prefix = f'weather_data/{custom_time}' #edit this to get current date's file (using prefix)
        local_directory = f'{os.getcwd()}/Python/Project/files/' #local directory to store files
        #process : delete folder, create folder, download files into the folder
        del_folder(local_directory)
        create_folder(local_directory)
        download_file(bucket_name,prefix, local_directory)

        combined_files = combine_csv_files(local_directory)
        dat, prediction = machine_learning(combined_files)
        #data every minute
        #uploading data to sql
        db_up(prediction, dat)#sql upload cell
        print('Refreshes in 1 minute')
        time.sleep(60)


    
main()
