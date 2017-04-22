# Assignment 11
three files: assignment file, function file, test file.

# Assignment 10
There is a little issue that user has to enter an input right after using command "mpiexec -n 5 python mpi_assignment_2.py".

# xc918_assignment6

Before changing anything, the result is 
Before(cProfile): 1049010 function calls (1046930 primitive calls) in 1.897 seconds
Before(line_profiler):
Timer unit: 1e-06 s

Total time: 2.7973 s
File: calculator1.py
Function: hypotenuse at line 45

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    45                                           def hypotenuse(x,y):
    46                                               """
    47                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    48                                               x and y must be two-dimensional arrays of the same shape.
    49                                               """
    50         1       736718 736718.0     26.3      xx = multiply(x,x)
    51         1       729139 729139.0     26.1      yy = multiply(y,y)
    52         1       708603 708603.0     25.3      zz = add(xx, yy)
    53         1       622838 622838.0     22.3      return sqrt(zz)

    

After changing some functions in calculator.py, the result is

After(cProfile): 48998 function calls (46918 primitive calls) in 0.150 seconds
After(line_profiler):
Timer unit: 1e-06 s

Total time: 0.010062 s
File: calculator.py
Function: hypotenuse at line 36

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    36                                           def hypotenuse(x,y):
    37                                               """
    38                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    39                                               x and y must be two-dimensional arrays of the same shape.
    40                                               """
    41                                               # xx = x*x
    42                                               # yy = y*y
    43                                               # zz = xx + yy
    44         1         2735   2735.0     27.2      xx = multiply(x,x)
    45         1         2777   2777.0     27.6      yy = multiply(y,y)
    46         1         2529   2529.0     25.1      zz = add(xx,yy)
    47         1         2021   2021.0     20.1      return np.sqrt(zz)








# xc918_assignment3

Assignment3 from Xing Cui(xc918).

Reducing function call overhead: removed uncleaned functions and added into advanced and report_energy. Big improvement.

Using alternatives to membership testing of lists: For the nbody_2, I changed list to set, which is faster. After the last improvement, I could remove it since we do not need to check any more. There were improvement.

Using local rather than global variables: Added BODIES as local variables.

Using data aggregation to reduce loop overheads: In order to improve speed, we could save some checking time since it is unnecessary once we have all pair of names.


# xc918_assignment4

Code review team member:

Reviewers:

Hao Liu (hl2514)

Yuting Gui (yg1281)

Reviewee:

Xing Cui (xc918)

One thing corrected in the nbody_opt.py to correct the outputs.



# xc918_assignment5

Added three files, and they are:
nbody_iter.py
binary.py
test.py
