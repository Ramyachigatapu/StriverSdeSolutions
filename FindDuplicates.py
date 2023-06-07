
from sys import *
from collections import *
from math import *


def findDuplicate(arr: list, n: int):
    d = {}
    for i in arr:
        if i in d:
            return i
        else:
            d[i] = 1

    # Write your code here.
    # Returns an integer.
    pass
