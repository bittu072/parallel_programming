# example of multiprocessing (this is the example of the shared memory between parent and child process using queue)
# creating separate processes for each task

import time
import multiprocessing

def square_num(num_array, q):
    for num in num_array:
        q.put(num*num)
    return

num_array=[25,2,7,56,98]

q1 = multiprocessing.Queue()
p1 = multiprocessing.Process(target=square_num, args=(num_array,q1))

p1.start()

p1.join()

print("Queue:")
while q1.empty() is False:
    print (q1.get())

print ("multiprocessing done!!!")
