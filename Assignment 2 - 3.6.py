#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:03:20 2020

@author: gabecagnazzi
"""


#Assignment 2-3.6: Turing Test

input("What is your problem? ")

userInput = str(input("Have you had this problem before (yes or no)? "))

if userInput == 'yes':
    print("Well, you have it again.")
else:
    print("Well, you have it now.")
    
# answer to the follow up question: this conversation would most likely not 
#convince the user that the entity on the other end exhibited intelligent behavior 
# because it did not help them with their problem merely gave scripted responses
# with zero artificial thinking done by the computer
    