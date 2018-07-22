#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:32:28 2018

@author: abhijith
"""

import pandas as pd  
import matplotlib  
import matplotlib.pyplot as plt  
import numpy as np  


df=pd.read_csv('weather_added_features.csv',index_col=0)
cor=df.corr()[['minTemp']].sort_values('minTemp')
cor2=df.corr()[['maxTemp']].sort_values('maxTemp')

predictors_mintemp=['pressure_1','pressure_2','pressure_3','dewPoint_1',
                    'dewPoint_2','dewPoint_3','minTemp_1',
                    'minTemp_2','minTemp_3'
                    ]

#
#predictors_maxtemp=['humidity_1','humidity_2','humidity_3',
#                    'cloudCover_1','cloudCover_2',
#                    'maxTemp_1', 'maxTemp_2', 'maxTemp_3',
#                   ]



predictors_maxtemp=['humidity_1','humidity_2','humidity_3',
                    'cloudCover_1','cloudCover_2','cloudCover_3',
                    'maxTemp_1', 'maxTemp_2', 'maxTemp_3']

df_minTemp=df[['minTemp']+predictors_mintemp]
df_maxTemp=df[['maxTemp']+predictors_maxtemp]


plt.rcParams['figure.figsize'] = [16, 22]
fig, axes = plt.subplots(nrows=3, ncols=3, sharey=True)
arr1 = np.array(predictors_maxtemp).reshape(3, 3)
arr2 = np.array(predictors_mintemp).reshape(3, 3)

for row, col_arr in enumerate(arr1):  
    for col, feature in enumerate(col_arr):
        axes[row, col].scatter(df_maxTemp[feature], df_maxTemp['maxTemp'])
        if col == 0:
            axes[row, col].set(xlabel=feature, ylabel='MaxTemp')
        else:
            axes[row, col].set(xlabel=feature)
plt.show()  

for row, col_arr in enumerate(arr2):  
    for col, feature in enumerate(col_arr):
        axes[row, col].scatter(df_minTemp[feature], df_minTemp['minTemp'])
        if col == 0:
            axes[row, col].set(xlabel=feature, ylabel='MinTemp')
        else:
            axes[row, col].set(xlabel=feature)
plt.show()  

