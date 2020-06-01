#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:14:43 2020

@author: gabecagnazzi
"""


#Assignment 2 - 2.12: 7% investment return

#intializing our variables
principal = 1000
rate = .07

#for 10 years
amount10 = principal * (1 + rate)**10

print(f"Amount after 10 years: {amount10: 10.2f}")


#for 20 years
amount20 = principal * (1 + rate)**20

print(f"Amount after 20 years: {amount20: 10.2f}")

#for 30 years
amount30 = principal * (1 + rate)**30

print(f"Amount after 30 years: {amount30: 10.2f}")