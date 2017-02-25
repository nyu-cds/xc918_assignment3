"""
    Assignment5
    Date: Feb 25.
    Author: Xing Cui
    NetID: xc918
"""


import itertools
import numpy as np
from itertools import permutations

def zbits(n, k):
	"""
	This is a program that takes two arguments n and k and prints all binary strings of length n that contain k zero bits, one per line.
	"""
	#define some inappropriate values.
    if n <= 0:
		print (ValueError)
		print ('n must be greater than 0.')
    elif k > n:
		print (ValueError)
		print ('It is better to have n is greater or equal to k.')
    else:
        zero_bucket = '0' * k
        one_bucket = '1' * (n - k)
        bucket =  zero_bucket + one_bucket
        string_bucket = []
        for item in permutations(bucket, n):
            string_bucket.append(''.join(item))
        string_bucket = set(np.unique(string_bucket))

        return string_bucket

