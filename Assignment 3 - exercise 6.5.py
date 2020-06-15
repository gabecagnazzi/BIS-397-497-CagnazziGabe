#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:45:42 2020

@author: gabecagnazzi
"""
# Please make sure your variables are defined correctly

#Exercise 6.5: Counting Duplicate Words

text = input("Enter text: ")
woord_counts = {}

for i in text.lower().split():
    if i in word_counts:
        woord-counts[i] += 1
    else: 
        woord_counts[i] = 1

print(f'{"WORD" : <12}COUNT')
    
for i, count in sorted(woord_counts.items()):
    print(f'{i: < 12}{count}')

