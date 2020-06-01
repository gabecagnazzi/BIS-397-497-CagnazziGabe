#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:22:18 2020

@author: gabecagnazzi
"""


#Assignment 2-3.10: 7% Investment return

principal = 1000
rate = .07

for year in range(1, 31):
#for 10 years
    amount10 = principal * (1 + rate)**year
    print(f"{year:>2}{amount10: 10.2f}")

