# pip install numpy
import numpy as np
import sys, time
# list - more memory, slow
# numpy - less memory, very fast


l = range(1000)                     # 14 bytes
#print(l)
#print(sys.getsizeof(6)*len(l))

a = np.arange(1000)                 # 4 bytes
#print(a)
#print(a.size*a.itemsize)


l1 = range(10000000)
l2 = range(10000000)
a1 = np.arange(10000000)
a2 = np.arange(10000000)
start= time.time()

end = time.time()
print("time taken by list - {}".format(end-start))
start= time.time()
resList = a1+a2
end = time.time()
print("time taken by nparray - {}".format(end-start))

a1 = np.array((2, 5, 7, 3))
a2 = np.array([12, 5, 70, 9])

print(a1+a2)
print(a1-a2)
print(a1*a2)
print(type(a1/a2))
