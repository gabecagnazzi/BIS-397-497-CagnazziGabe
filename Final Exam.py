#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:37:48 2020

@author: gabecagnazzi
"""

#BIS 397 Final Exam COVID-19 Cases in PA

import pandas as pd
import pickle
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


CT = pd.read_csv("us-states.csv")

#Converting Date from object to Date

CT['date'] = pd.to_datetime(CT['date'],infer_datetime_format=True)
CT['date']

#Process the DataFrame to keep only observations for Pennsylvania

CT['state'].describe()

CT['valid'] = CT['state'] == "Pennsylvania"

CT['valid'].describe()

CT[['state','valid']].head()

CT = CT[CT.valid == True]

CT

#Create a new series in the Data Frame entitled "adj_deaths"
#filling that series with the values in "deaths"

CT['adj_deaths'] = CT['deaths']

#April 21st, 2020 deaths should be adjusted downward by 282
CT['adj_deaths'].describe()

CT.loc[CT['date'] == "2020-4-21" , 'adj_deaths'] -= 282

CT['adj_deaths'].describe()

#April 22nd, 2020 deaths should be adjusted downward by 297
CT['adj_deaths'].describe()

CT.loc[CT['date'] == "2020-4-22" , 'adj_deaths'] -= 297

CT['adj_deaths'].describe()

#graphing portion 

plt.style.available[:20]
plt.style.use('bmh')

plt.bar(CT['date'], CT['adj_deaths'], color = 'darkslategrey')
plt.xlabel('Date',fontsize=15)
plt.ylabel('Deaths',fontsize=15)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("PA Coronavirus Deaths", fontsize=15)
plt.show()


          
