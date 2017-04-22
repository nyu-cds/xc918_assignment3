'''
Author: Xing Cui
Date: Apr 22, 2017

This file contains functions that do splitting list of numbers and sort them.
'''
import numpy as np
from mpi4py import MPI
import bisect

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def splitting(nums, size):
	"""spliting number list by size
	"""
	coverage = max(nums) - min(nums)
	tmp = np.array_split(np.asarray(range(coverage+1)), size)
	for x in tmp:
		max_nums = [max(x)]
	return max_nums

def sorting(nums, max_nums, size):
	"""sorting numbers
	"""
	sorting = []
	sorting.append([x for x in nums if x in range(min(nums), max_nums[0]+1)])
	for i in range(1, size):
		last_max = max_nums[i-1]
		sorting.append([x for x in nums if x in range(last_max + 1, max_nums[i]+1)])
	return np.asarray(sorting)





	

