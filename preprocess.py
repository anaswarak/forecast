#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 20:33:16 2018

@author: abraham
"""

from datetime import datetime, timedelta  
import time  
from collections import namedtuple  
import pandas as pd  
import matplotlib.pyplot as plt  


df2=pd.read_hdf('weather_frame.h5','df')
