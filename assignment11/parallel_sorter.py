'''
Author: Xing Cui
Date: Apr 22, 2017

This file is the ask user to input a integer that indicates how many numbers to sort.
'''
import numpy as np
from functions import *
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
n = input('input how many numbers you want to sort: ')
n = int(n)
nums = [np.random.randint(0,n*3) for i in range(n)]

if rank == 0:
	if len(nums) < 2:
		raise ValueError
		print 'Oops, value error found. Need at least 2 numbers.'
	else:
		max_nums = splitting(nums, size) # see splitting function in functions.py
		result = sorting(nums, max_nums, size) # see sorting function in functions.py
else:
	result = None

result = comm.scatter(result, root = 0)
final_result = comm.gather(np.sort(result), root=0)

if rank == 0:
	final_result = np.concatenate(final_result)

if __name__ == '__main__':
	print(final_result)


