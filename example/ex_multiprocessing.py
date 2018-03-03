# example of multiprocessing
# creating separate processes for each task

import time
import multiprocessing

def square_num(num_array):
    for num in num_array:
        time.sleep(0.2)
        print ("square of " + str(num) + " is : " + str(num*num))
    return


def cube_num(num_array):
    for num in num_array:
        time.sleep(0.2)
        print ("cube of " + str(num) + " is: " + str(num*num*num))
    return

num_array=[25,2,7,56,98]

p1 = multiprocessing.Process(target=square_num, args=(num_array,))
p2 = multiprocessing.Process(target=cube_num, args=(num_array,))

# starting the threads
p1.start()
p2.start()

# join will tell compiler to wait here until p1 and p2 gets done
p1.join()
p2.join()

print ("multiprocessing done!!!")
