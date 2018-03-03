# example of multiprocessing (this is the example of the shared memory between parent and child process)
# creating separate processes for each task

import time
import multiprocessing

def square_num(num_array, final):
    for index, num in enumerate(num_array):
        print ("square of " + str(num) + " is : " + str(num*num))
        final[index]=num*num
    return

num_array=[25,2,7,56,98]

final_sqr = multiprocessing.Array('i',5) ### multiprocessing.Array('data_type',array_size)
p1 = multiprocessing.Process(target=square_num, args=(num_array,final_sqr))

# starting the threads
p1.start()

# join will tell compiler to wait here until p1 and p2 gets done
p1.join()

print("final: " + str(final_sqr[:]))
print ("multiprocessing done!!!")


# in non-shared example, even global defined variable can not be used in parent, but it can be used in child
