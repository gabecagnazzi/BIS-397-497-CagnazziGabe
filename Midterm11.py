#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:59:47 2020

@author: gabecagnazzi
"""

import random

def roll_dice1():
    die1 = random.randrange(1, 7)
    return (die1)  # pack die face values into a tuple
def roll_dice2():
    die2 = random.randrange(1, 7)
    return (die2)  # pack die face values into a tuple
def roll_dice3():
    die3 = random.randrange(1, 7)
    return (die3)  # pack die face values into a tuple
def roll_dice4():
    die4 = random.randrange(1, 7)
    return (die4)  # pack die face values into a tuple
def roll_dice5():
    die5 = random.randrange(1, 7)
    return (die5)  # pack die face values into a tuple

def display_dice(die_values1, die_values2, die_values3, die_values4, die_values5):
    """Display one roll of the five dice."""  
    print(die_values1, die_values2, die_values3, die_values4, die_values5)

die_values1 = roll_dice1()  # first roll


die_values2 = roll_dice2()  # first roll


die_values3 = roll_dice3()  # first roll


die_values4 = roll_dice4()  # first roll


die_values5 = roll_dice5()  # first roll

print("Results of first roll: ")
display_dice(die_values1, die_values2, die_values3, die_values4, die_values5)

userInput = 0

while userInput != -99:
       userInput = int(input("Enter the dice you want to roll again, enter -99 if you are done chosing: "))
       if userInput == 1:
           die_values1 = roll_dice1()
       elif userInput == 2:
           die_values2 = roll_dice2()
       elif userInput == 3:
           die_values3 = roll_dice3()
       elif userInput == 4:
           die_values4 = roll_dice4()
       elif userInput == 5:
           die_values5 = roll_dice5()
   

print("Results of second roll: ")
display_dice(die_values1, die_values2, die_values3, die_values4, die_values5)

userInput = 0

while userInput != -99:
       userInput = int(input("Enter the dice you want to roll again, enter -99 if you are done chosing: "))
       if userInput == 1:
           die_values1 = roll_dice1()
       elif userInput == 2:
           die_values2 = roll_dice2()
       elif userInput == 3:
           die_values3 = roll_dice3()
       elif userInput == 4:
           die_values4 = roll_dice4()
       elif userInput == 5:
           die_values5 = roll_dice5()

print("Results of third roll: ")
display_dice(die_values1, die_values2, die_values3, die_values4, die_values5)           