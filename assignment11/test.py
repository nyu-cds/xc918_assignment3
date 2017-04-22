'''
Author: Xing Cui
Date: Apr 22, 2017

This is test.py to test all functions in functions.py.
'''

import numpy as np
import unittest
from mpi4py import MPI
from functions import *

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class TestSort(unittest.TestCase):
 
    def set(self):
        pass
        
    def test_splitting(self):
        assert splitting([8,4,3,6,5,2,1,9,7], 4) == [8]
        
    def test_sorting(self):
        assert sorting([8,4,3,6,5,2,1,9,7], [3,7,11], 3).tolist() == np.array([[3,2,1],[4,6,5,7],[8,9]]).tolist()
        


if __name__ == '__main__':
    unittest.main()