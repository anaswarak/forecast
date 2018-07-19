from datetime import datetime, timedelta  
import time  
from collections import namedtuple  
import pandas as pd  
import requests  
import matplotlib.pyplot as plt  

features=['startdate','datadate','maxTemp','minTemp','pressure','humidity', 'percipIntensity', 'percipProbablity',
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
        records.append(
            DailySummary(
                
                    startdate=currentDay,
                    datadate=NthDay,
                    maxTemp=data['temperatureHigh'],
                    minTemp=data['temperatureLow'],
                    pressure=data['pressure'],
                    humidity=data['humidity'],
                    percipIntensity=data['precipIntensity'],
                    percipProbablity=data['precipProbability'],
                    visibility=data['visibility'],
                    dewPoint=data['dewPoint'],
                    cloudCover=data['cloudCover'],
                    windSpeed=data['windSpeed'],
                    windBearing=data['windBearing'] ,
                    icon=data['icon'],

                
            )
        )
    return records


API_KEY="7269dadac7cbcf758679688711acf4ab"
sampleLat="9.9312"
sampleLong="76.2673"

BASE_URL="https://api.darksky.net/forecast/{}/{},{},{}?exclude=currently,flags,hourly"

currDate=datetime.now()
N=7

# print(str(currDate.timestamp()))
# a=str(currDate.timestamp())
# a=a[:a.index('.')]
# print(a)
record=extractData(BASE_URL,API_KEY,sampleLat,sampleLong,datetime.now(),N)
print(record)

