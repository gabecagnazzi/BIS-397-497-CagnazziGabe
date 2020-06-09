#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:04:29 2020

@author: gabecagnazzi
"""


# exercise 5.15: Tuples representing Invoices

from operator import itemgetter

invoice = (("83", "Electric sander", 7,57.98),("24", "power saw",
                                               18, 99.99), 
           ("7", "Sledge hammer", 11,21.50), ("77","Hammer", 76, 11.99),
           ("'39", "Jig Saw", 3,79.50))

print("invoice sorted by item description: ")
print(sorted(invoice,key = itemgetter(1)))
print()
print("invoice sorted by item price: ")
print(sorted(invoice,key = itemgetter(3)))
print()
print("----------invoice tuple containing part description and quantity----------")

x = ()

for i in invoice: 
    temp1 = ((i[1],i[2]))
    x+= (temp1,)
    
print(sorted(x,key=itemgetter(1)))
print()
print("----------invoice tuple containing part description and value----------")

y = ()

for i in invoice:
    temp2 = (i[1], i[2] * i[3])
    y+= (temp2, )

print(sorted(y,key = itemgetter(1)))
print()

for i in y:
    if i[1] >= 200 and i[1] <= 500:
        print(i)
        
print()
total = 0

for i in y:
    total += i[1]

print("total value is equal to: ", total)    
    
    
    
