#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:34:51 2020

@author: gabecagnazzi
"""

#Assignment 2 - 4.9: Temperature Conversion

def Farenheit (C):
    #conversion
    return(9.0/5) * C + 32

print("Celsius\tFarenheit")
#from 1 to 100
for x in range(0, 101):
    print(x, "\t", round(Farenheit(x), 1))
    