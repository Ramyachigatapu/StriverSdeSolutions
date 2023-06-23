from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	hm = {}
	maj = floor(n / 2)
	for i in arr:
		if i in hm:
			hm[i] += 1
		else:
			hm[i] = 1
	for i in hm:
		if hm[i] > maj:
			return i
	return -1
	# Write your code here.
	pass