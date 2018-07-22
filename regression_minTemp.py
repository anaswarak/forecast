#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:31:35 2018

@author: abhijith
"""

from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from training import df_minTemp, predictors_mintemp

X=df_minTemp[predictors_mintemp]
y=df_minTemp['minTemp']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                 test_size=0.2, random_state=12) 

regressor = LinearRegression()
regressor.fit(X_train, y_train)
prediction = regressor.predict(X_test)
# Evaluate the prediction accuracy of the model
from sklearn.metrics import mean_absolute_error, median_absolute_error  
print("The Explained Variance: %.2f" % regressor.score(X_test, y_test))  
print("The Mean Absolute Error: %.2f farenheit" % mean_absolute_error(y_test, prediction))  
print("The Median Absolute Error: %.2f farenheit" % median_absolute_error(y_test, prediction))  