"""
Before(cProfile): 1049010 function calls (1046930 primitive calls) in 1.897 seconds
Before(line_profiler):
Timer unit: 1e-06 s

Total time: 2.7973 s
File: calculator1.py
Function: hypotenuse at line 45

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    45                                           def hypotenuse(x,y):
    46                                               
    47                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    48                                               x and y must be two-dimensional arrays of the same shape.
    49                                               
    50         1       736718 736718.0     26.3      xx = multiply(x,x)
    51         1       729139 729139.0     26.1      yy = multiply(y,y)
    52         1       708603 708603.0     25.3      zz = add(xx, yy)
    53         1       622838 622838.0     22.3      return sqrt(zz)

    



After(cProfile): 48998 function calls (46918 primitive calls) in 0.150 seconds
After(line_profiler):
Timer unit: 1e-06 s

Total time: 0.010062 s
File: calculator.py
Function: hypotenuse at line 36

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    36                                           def hypotenuse(x,y):
    37                                               
    38                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    39                                               x and y must be two-dimensional arrays of the same shape.
    40                                               
    41                                               # xx = x*x
    42                                               # yy = y*y
    43                                               # zz = xx + yy
    44         1         2735   2735.0     27.2      xx = multiply(x,x)
    45         1         2777   2777.0     27.6      yy = multiply(y,y)
    46         1         2529   2529.0     25.1      zz = add(xx,yy)
    47         1         2021   2021.0     20.1      return np.sqrt(zz)
"""


# -----------------------------------------------------------------------------
# calculator_test.py
# ----------------------------------------------------------------------------- 
import numpy as np
import calculator as calc

M = 10**3
N = 10**3

A = np.random.random((M,N))
B = np.random.random((M,N))

calc.hypotenuse(A,B)
#lprun -f calc.hypotenuse(A,B)
