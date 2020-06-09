#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:02:30 2020

@author: gabecagnazzi
"""


#Exercise 6.8: Challenge: Writing the word equivalent of a check amount

# A function that prints
# given number in words
def convert_to_words(num):
  
   
   l = len(num);

   
   if (l == 0):
       print("empty string");
       return;

  
   if (l > 4):
       print("Length more than 4 is not supported");
       return;

   # The first string is not used,
   # it is to make array indexing simple
   single_digits = ["zero", "one", "two", "three",
                   "four", "five", "six", "seven",
                   "eight", "nine"];

   # The first string is not used,
   # it is to make array indexing simple
   two_digits = ["", "ten", "eleven", "twelve",
               "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen",
               "nineteen"];

   # The first two string are not used,
   # they are to make array indexing simple
   tens_multiple = ["", "", "twenty", "thirty", "forty",
                   "fifty", "sixty", "seventy", "eighty",
                   "ninety"];

   tens_power = ["hundred", "thousand"];

  
   # For single digit number
   if (l == 1):
           print(single_digits[ord(num[0]) - '0']);
           return;
    
       # Iterate while num is not '\0'
   x = 0;
   while (x < len(num)):
          
       # Code path for first 2 digits
       if (l >= 3):
           if (ord(num[x]) - 48 != 0):
                   print(single_digits[ord(num[x]) - 48],
                                           end = " ");
                   print(tens_power[l - 3], end = " ");
                   # here len can be 3 or 4
                  
           l -= 1;
              
           # Code path for last 2 digits
       else:
              
               
               # array of strings
              if (ord(num[x]) - 48 == 1):
                   sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48);
                      
                   print(two_digits[sum] , end = " ");
                   return;
    
               # Need to explicitely handle 20
              elif (ord(num[x]) - 48 == 2 and
                   ord(num[x + 1]) - 48 == 0):
                   print("twenty", end = " ");
                   return;
                  
               # Rest of the two digit
               # numbers i.e., 21 to 99
              else:
                   i = ord(num[x]) - 48;
                   if(i > 0):
                       print(tens_multiple[i], end = " ");
                   else:
                       print("", end = "");
                   x += 1;
                   if(ord(num[x]) - 48 != 0):
                       print(single_digits[ord(num[x]) - 48], end = " ");
       x += 1;




# Take input from user
amount = input("Enter Amount : ")

# Split the before and after decimal parts
amount_num = amount.split('.')

# Convert the before decimal part to words
convert_to_words(amount_num[0]);

# Print the after decimal part
if(len(amount_num[1]) == 1):
    print("and "+ amount_num[1] + '0/100')
else:
    print("and "+ amount_num[1] + '/100')