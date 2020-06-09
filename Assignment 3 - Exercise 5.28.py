#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:32:35 2020

@author: gabecagnazzi
"""


#Exercise 5.28: Intro to Data Science survey response statitistics

import numpy as np
import statistics

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

u_elements, count_elements = np.unique(responses, return_counts=True)

print("Frequency of responses: ")

for i in range(len(u_elements)):
    print("there are ", responses[i], "with values of ", count_elements[i])
    
print("\n\nThe statistics are: ")
print("Min: ", min(responses))
print("Max: ", max(responses))
print("Range: ", max(responses) - min(responses))
print("Median: ", statistics.median(responses))
print("Mode: ", statistics.mode(responses))
print("Variance: ", statistics.variance(responses))
print("Standard Deviation: ", statistics.stdev(responses))

