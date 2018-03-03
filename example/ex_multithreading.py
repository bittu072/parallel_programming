# example of multithreading

import time
import threading

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

# ########### non-multithreading
t = time.time()
square_num(num_array)
cube_num(num_array)

print ("time taken to finish two task: ",(time.time() - t))
print ("non-multithreading task is done!!!")


########### multithreading
t1=time.time()
th1=threading.Thread(target=square_num, args=(num_array,))
th2=threading.Thread(target=cube_num, args=(num_array,))

# starting the threads
th1.start()
th2.start()

# join will tell compiler to wait here until th1 and th2 gets done
th1.join()
th2.join()


print ("time taken to finish two task with multithreading: ",(time.time() - t1))
print ("multithreading task is done!!!")
