from datetime import datetime, timedelta  
import time  
from collections import namedtuple  
import pandas as pd  
import requests
import matplotlib.pyplot as plt  
import pickle

features=['date','maxTemp','minTemp','pressure','humidity',
'visibility','dewPoint','cloudCover','windSpeed','windBearing', 'icon']
DailySummary=namedtuple("DailySummary",features)

def extractData(url,key,lat,lon, startingDay, days):
    records=[]
    currentDay=startingDay
    for i in range(days):
        NthDay=currentDay-timedelta(i)
        epochTime=str(NthDay.timestamp())
        epochTime=epochTime[:epochTime.index('.')]
        request=url.format(key,lat,lon,epochTime)
        response=requests.get(request)
        data=response.json()['daily']['data'][0]
        if response.status_code==200:
            records.append(
                DailySummary(
                    
                        date=NthDay,
                        maxTemp=data['temperatureHigh'],
                        minTemp=data['temperatureLow'],
                        pressure=data['pressure'],
                        humidity=data['humidity'],
                        #precipIntensity=data['precipIntensity'] ? data['precipIntensity']: 0,
                        #precipProbablity=data['precipProbability'],
                        visibility=data['visibility'],
                        dewPoint=data['dewPoint'],
                        cloudCover=data['cloudCover'],
                        windSpeed=data['windSpeed'],
                        windBearing=data['windBearing'] ,
                        icon=data['icon'],

                    
                )
            )
    return records
   
sampleLat="9.9312"
sampleLong="76.2673"

BASE_URL="https://api.darksky.net/forecast/{}/{},{},{}?exclude=currently,flags,hourly"

currDate=datetime.now()
N=90

record=pickle.load(open('weather_data.p', 'rb'))
df = pd.DataFrame(record, columns=features).set_index('date') 
df.to_csv('weather_frame.csv')
df.to_hdf('weather_frame.h5','df')

#iconDict={"wind":1, "rain":3, "partly-cloudy-day":2, "fog":4,
#          "partly-cloudy-night":2}
#a=df.describe() 
#print(df.dtypes)
#tmp = df[['maxTemp', 'dewPoint', 'icon']].tail(10)  
#
#df2=df.copy()
#df2=df2.replace({"icon":iconDict})

# print("record2 is")
# # print(record2)

