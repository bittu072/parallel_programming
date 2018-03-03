# example of locking in multiprocessing

import time
import multiprocessing

def add_car_to_inventory(car_count, lck):
    for i in range(0,100):
        lck.acquire()
        car_in_stock.value = car_in_stock.value + 1
        lck.release()
    return


def car_sold(car_count, lck):
    for i in range(0,50):
        lck.acquire()
        car_in_stock.value = car_in_stock.value - 1
        lck.release()
    return

car_in_stock = multiprocessing.Value('i',500)
lock = multiprocessing.Lock()
p1 = multiprocessing.Process(target=add_car_to_inventory, args=(car_in_stock, lock))
p2 = multiprocessing.Process(target=car_sold, args=(car_sold, lock))

# starting the threads
p1.start()
p2.start()

# join will tell compiler to wait here until p1 and p2 gets done
p1.join()
p2.join()

print ("car in stock: " + str(car_in_stock.value))
# output should be 550 always....but if we do not add locks then it can have random value sometime

print ("multiprocessing done!!!")
