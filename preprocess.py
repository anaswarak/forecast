#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta  
import time  
from collections import namedtuple  
import pandas as pd  
import matplotlib.pyplot as plt  




def derive_nth_day_feature(df, feature, N):  
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N, rows)]
    col_name = "{}_{}".format(feature, N)
    df[col_name] = nth_prior_measurements

    
df1 = pd.read_csv('weather_frame.csv',index_col=0)
df=df1.drop(labels='icon', axis=1)

features=['date','maxTemp','minTemp','pressure','humidity',
'visibility','dewPoint','cloudCover','windSpeed','windBearing']

for feature in features:  
    if feature != 'date':
        for N in range(1, 4):
            derive_nth_day_feature(df, feature, N)

spread = df.describe().T
IQR = spread['75%'] - spread['25%']
spread['outliers'] = (spread['min']<(spread['25%']-(3*IQR)))|(spread['max'] > (spread['75%']+3*IQR))
print(spread.loc[spread.outliers,])


plt.rcParams['figure.figsize'] = [14, 8]
df.humidity_1.hist()
plt.title('Distribution of humidity_1')
plt.xlabel('humidity_1')
plt.show() 

df.pressure_1.hist()
plt.title('Distribution of pressure_1')
plt.xlabel('pressure_1')
plt.show()