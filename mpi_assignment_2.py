import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1)

        
if rank == 0:
        user_input = input('Process 0 needs an integer from 0 to 100: ')
        # check for valid user input
        try:
            if user_input <0 or user_input >100:
                raise ValueError
                print 'Process does not accept integers out of range or non-integers. Now setting to 0.'
                user_input = 0
            else:
                user_input = int(user_input)

        except ValueError:
            print 'Process does not accept integers out of range or non-integers. Now setting to 0.'
            user_input = 0


        randNum[0] = user_input
        print("Process", rank, "received the number", randNum[0])
        req_send = comm.Isend(randNum, dest=rank+1)
        req_send.Wait()
        print("Process", rank, "sent the number", randNum[0])

else:
    # Process i+1 receives value from previous Process 
    req_rec = comm.Irecv(randNum, source=rank-1)
    req_rec.Wait()
    print("Process", rank, "received the number", randNum[0])
    # Process i+1 multiplies input value with i+1
    randNum *= rank 
    try:
        req_send = comm.Isend(randNum, dest=rank+1)
        req_send.Wait()
        print("Process", rank, "received the number", randNum[0])
    except:
        pass
