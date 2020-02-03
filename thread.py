# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:33:49 2020

@author: skondaveti
"""

# requests module

import threading as th
import math
import time

def computeExponetnValue(x,y):
    res=pow(x,y)
    print("res is {}".format(res))

def sqrt(x):
    res=math.sqrt(x)
    print("sqrt res is {}".format(res))
    
if __name__ == "__main__":
    start_time=time.time()
    computeExponetnValue(4,6)
    sqrt(100)
    end_time=time.time()
    print("exection time is {}".format(end_time-start_time))