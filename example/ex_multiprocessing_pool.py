from multiprocessing import Pool
import time



def func_xyz(n):
    final_num = 0
    n=999999
    for i in range(999999):
        final_num = final_num + (i * n)
        n = n - 1
    return final_num

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    output = p.map(func_xyz,range(1))
    p.close()
    p.join()

    print(output)
    print ("time taken using pool: ", time.time() - t1)

    t2 = time.time()
    abcd = func_xyz(1)
    print(abcd)
    print ("time for non-pool: ", time.time() - t1)
