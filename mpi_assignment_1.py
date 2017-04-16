from mpi4py import MPI
comm = MPI.COMM_WORLD
# get the rank for this process
rank = comm.Get_rank()

#check for even and odd
if rank%2 == 0: 
        print("Hello from process {}".format(rank))

if rank%2 == 1: 
        print("Goodbye from process {}".format(rank))
