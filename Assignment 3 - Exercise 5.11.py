#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:24:32 2020

@author: gabecagnazzi
"""

# 5.11 Sumnmarizing Letters in a String

alphabet = "abcdefghijklmnopqrstuvwxyz"

def summarize_letters(string):
    char_counter = ()
    string_lc =string.lower()
    
    for i in string_lc:
        if i in char_counter and i.isalpha():
            char_counter[i] = char_counter[i] + 1
        if i not in char_counter and i.isalpha():
            char_counter[i] = 1

    list_tuples = [(k, v) for k, v in char_counter.items()]
    return list_tuples
            
    

alphabets = 'a b b b b B A c e f g d h i j k B l m M n o p q r s P t u v w x y z'
print(summarize_letters(alphabets))


import string

alphabet = set(string.ascii_lowercase)
#checking if our hardcoded string has all the letters
if set(alphabets.lower()) >= alphabet:
    print('The string ' +alphabets+' has all the letters in the alphabet ')