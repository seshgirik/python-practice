# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:50:10 2020

@author: skondaveti
"""

def fibfun(limit):
    i=0
    while(i<limit):
        
        if i==0:
            a=0
            b=1
        
        fib=a+b
        yield fib
        a=b
        b=fib
        
        i=i+1
        
        
        
        
x=fibfun(10)
for element in x.__iter__():
    print(element)
#print(x)
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#

    