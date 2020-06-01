#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:40:08 2020

@author: gabecagnazzi
"""

#Assignment 2 - 3.1: Validating User Input

passes = 0  # number of passes
failures = 0  # number of failures
count = 0

# process 10 students
while count != 10:
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1
        count += 1
    elif result == 2:
        failures = failures + 1
        count += 1
    else:
        print("Please enter either 1 or 2: ")
    

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
