#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:46:15 2020

@author: gabecagnazzi
"""


#Simulation: The Tortoise and the Hare

import random

Race_End = 70

def move_tortoise(tortoise):
    #moving tortoises position
    move = random.randrange(1,11) #random chose
    
    #percentage moves
    if 1 <= move <= 5: #fast plod
        tortoise += 3
    elif move in (6,7): #slip down
        tortoise -= 6
    else: #slow mans
        tortoise += 1
    
    
    #ensureing tortoise doesnt slip past start or finish
    if tortoise < 1:
        tortoise = 1
    elif tortoise > Race_End:
        tortoise = Race_End
    
    return tortoise

def move_hare (hare):
    #moving hare's position
    move = random.randrange(1,11) #randomizing move
    
    #percent moves
    if move in (3,4): # big stepper
        hare += 9
    elif move == 5: #big slip
        hare -= 12
    elif 6 <= move <= 8: #smol hop
        hare += 1
    elif move > 8: #smol slip
        hare -= 2
    
    #slip past start/finish
    if hare < 1:
        hare = 1
    elif hare > Race_End:
        hare = Race_End
    
    return hare

def print_positions(tortoise, hare):
    #displaying positions of tort and hare. goes through all 70 printing t and h
    
    for count in range(1, Race_End + 1):
        if count == tortoise and count == hare:
            print("OUCH!!!", end='')
        elif count == hare:
            print("H", end='')
        elif count == tortoise:
            print("T", end= '')
        else:
            print(' ', end='')
        
        
    print()
    
#running race
tortoise = 1
hare = 1
timer = 0

print("ON YOUR MARK, GET SET")
print("BANG !!!!!")
print("AND THEY'RE OFF !!!!!")

while tortoise < Race_End and hare < Race_End:
    hare = move_hare(hare)
    tortoise = move_tortoise(tortoise)
    print_positions(tortoise, hare)
    timer += 1

if tortoise >= hare:
    print("\nTORTOISE WINS!!! YAY!!!")
else:
    print("\nHare wins. Yuch!")

print(f"TIME ELAPSED = {timer} seconds")
    




