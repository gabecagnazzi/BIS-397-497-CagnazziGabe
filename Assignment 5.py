# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:19:49 2020

author: Troy Adair
"""

import pandas as pd

# Read in csv file from first script
YT = pd.read_csv("Yellow_Saved.csv")

# Look at DataFrame
YT

# DataFrames are constructed of columns called Series. To see columns:
YT.columns

# Looking at dtypes
YT.dtypes

# pickup, dropoff, and duration were stored as strings!!!!
# Let's convert them back to datetimes
YT['pickup'] = pd.to_datetime(YT['pickup'],
                              infer_datetime_format=True)


YT['dropoff'] = pd.to_datetime(YT['dropoff'],
                              infer_datetime_format=True)

YT['duration'] = pd.to_datetime(YT['duration'],
                              infer_datetime_format=True)


YT[['pickup','dropoff','duration']].head()

# Let's look for other problematic values

YT.describe()

YT.columns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

YT['passenger_count'].describe()

YT['trip_distance'].describe()

YT['fare_amount'].describe()

YT['extra'].describe()

YT['mta_tax'].describe()

YT['tolls_amount'].describe()

YT['improvement_surcharge'].describe()

YT['total_amount'].describe()

# Rules we agree to
# trip_distance <= 100 (already implemented)

# delete any rows where passengers = 0 
YT['passenger_count'].describe()

YT['valid'] = YT['passenger_count'] == 0

YT['passenger_count'].describe()

YT = YT[YT.valid == False]

YT['passenger_count'].describe()

# delete trip distance = 0
YT['trip_distance'].describe()

YT['validC'] = YT['trip_distance'] == 0

YT['trip_distance'].describe()

YT = YT[YT.validC == False]

YT['trip_distance'].describe()

# fare amount make greater than zero, lt 1,000
YT['fare_amount'].describe()

YT['validB'] = YT['fare_amount'] > 0

YT['fare_amount'].describe()

YT = YT[YT.validB == True]

YT['fare_amount'].describe()

YT['validTwo'] = YT['fare_amount'] <= 1000

YT['fare_amount'].describe()

YT = YT[YT.validTwo == True]

YT['fare_amount'].describe()

# make "extra" >= 0
YT['extra'].describe()

YT['validA'] = YT['extra'] >= 0

YT['extra'].describe()

YT = YT[YT.validA == True]

YT['extra'].describe()

#Provide descriptive data using the Pandas describe() function on the remaining observations.
YT['passenger_count'].describe()

YT['trip_distance'].describe()

YT['fare_amount'].describe()

YT['extra'].describe()

YT['mta_tax'].describe()

YT['tolls_amount'].describe()

YT['improvement_surcharge'].describe()

YT['total_amount'].describe()

# Saving our altered data set

YT.to_csv('YT_Curated.csv', index = False)
