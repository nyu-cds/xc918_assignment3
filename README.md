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