from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    hm = [0]*(n+1)
    for i in range(n):
        hm[arr[i]] += 1
    repeat , miss = -1, -1
    for i in range(1, n+1):
        if hm[i] == 2:
            repeat = i
        elif hm[i] == 0:
            miss = i
        if repeat != -1 and miss != -1:
            break
    return [miss, repeat]
    
    # Write your code here
    pass
