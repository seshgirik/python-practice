import threading as th
import math
import time

def computeExponentValue(x , y):
    for i in range(10):
        time.sleep(3)
        res = pow(x,y)
        print("computeExponentValue - res is {}".format(res))

def squrRoot(x):
    for i in range(20):
        time.sleep(1)
        res = math.sqrt(x)
        print("squrRoot - res is {}".format(res))

if __name__ == "__main__":
    start_time = time.time()
    # computeExponentValue(4, 6)
    # squrRoot(4096)
    t1 = th.Thread(target=computeExponentValue, args=(4,6))
    t2 = th.Thread(target=squrRoot, args=(4096,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print("Execution time is {}".format(end_time-start_time))