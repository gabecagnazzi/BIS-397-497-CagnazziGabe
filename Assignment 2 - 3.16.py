#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:48:39 2020

@author: gabecagnazzi
"""


#Assignment 2 - 3.16: Nested Control Statements

number1 = int(input("Enter 1st integer: "))
number2 = int(input("Enter 2nd integer: "))
number3 = int(input("Enter 3rd integer: "))
number4 = int(input("Enter 4th integer: "))
number5 = int(input("Enter 5th integer: "))
number6 = int(input("Enter 6th integer: "))
number7 = int(input("Enter 7th integer: "))
number8 = int(input("Enter 8th integer: "))
number9 = int(input("Enter 9th integer: "))
number10 = int(input("Enter 10th integer: "))

max1 = number1

for max1 in range (2):
    if number2 > max1:
        max1 = number2
    if number3 > max1:
        max1 = number3
    if number4 > max1:
        max1 = number4
    if number5 > max1:
        max1 =number5
    if number6 > max1:
        max1 = number6
    if number7 > max1:
        max1 = number7
    if number8 > max1:
        max1 = number8
    if number9 > max1:
        max1 = number9
    if number10 > max1:
        max1 = number10
    
    print(max1)
    
    if max1 == number1:
        number1 = 0
    if max1 == number2:
        number2 = 0
    if max1 == number3:
        number3 = 0
    if max1 == number4:
        number4 = 0
    if max1 == number5:
        number5 = 0
    if max1 == number6:
        number6 = 0
    if max1 == number7:
        number7 = 0
    if max1 == number8:
        number8 = 0
    if max1 == number9:
        number9 = 0
    if max1 == number10:
        number10 = 0
        
        
    