from math import *
from collections import *
from sys import *
from os import *

from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])
    r = [0] * n
    c = [0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                r[i] = 1
                c[j] = 1
    for i in range(n):
        for j in range(m):
            if r[i] or c[j]:
                matrix[i][j] = 0
        # Write your code here.
    pass
