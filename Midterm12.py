#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:11:26 2020

@author: gabecagnazzi
"""
import statistics
import random

def descriptive(numberList):
    mean = statistics.mean(numberList)
    median = statistics.median(numberList)
    stdev = statistics.stdev(numberList)
    pstdev = statistics.pstdev(numberList)
    
    print ("Mean is: ", mean)
    print ("Median is: ", median)
    print ("Sample Standard Dev. is: ", stdev)
    print ("Population Standard Dev. is: ", pstdev)
    
numberList = []
for number in range (10):
    rando = random.randrange(1,11)
    numberList.append(rando)
    
print(numberList)
descriptive(numberList)