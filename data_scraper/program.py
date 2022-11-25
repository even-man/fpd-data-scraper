import pandas as pd
import os
import datetime
import string
import requests


def main():

    #get dates
    todaysDate = str(datetime.date.today())
    todaysYear, todaysMonth, todaysDay = todaysDate.split('-')
    nextDay = int(todaysDay) + 1
    nextDay = str(nextDay)



    #url
    url = f"https://maps.fayetteville-ar.gov/DispatchLogs/json/getIncidents.cshtml/{todaysYear}-{todaysMonth}-{todaysDay}/{todaysYear}-{todaysMonth}-{nextDay}"

    #get data, store in dataframe
    r = requests.get(url)
    data = r.json()
    df = pd.json_normalize(data)

    #writing to csv file
    path = r"C:\Users\sdman\OneDrive\Desktop\Fpd_report_generator\Fpd_data.csv"
    df.to_csv(path, mode='a', index=False, header=None)
    


main()
