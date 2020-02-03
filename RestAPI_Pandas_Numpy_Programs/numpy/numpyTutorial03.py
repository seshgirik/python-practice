import numpy as np

# COPY Function
l = [56, 78, 89, 4, 11, 78, 65, 23, 43, 12, 31]
arr = np.array(l)
print(arr)
newarr = arr[5:].copy()
print(newarr)
newarr[2]= 100
print(newarr)
print(arr)

# Slicing
a = np.array([[2, 3, 4, 6, 7], [56, 78, 89, 4, 1], [72, 31, 56, 19, 82], [12, 13, 6, 21, 65]])

#  print(a)
#print(a[0])
#print(a[1])
#print(a[2])
#print(a[0,2])
#print(a[0:3,2:])
#print(a[:,1:])

#print(a[1:, 1:3])
#print(a[2, 1:4])
#print("np.linspace ::",np.linspace(2, 11, 10))

a = np.ones((4, 3), dtype='int32')
print("a          -\n {}".format(a))
print("type(a)    - {}".format(type(a)))
print("a.ndim     - {}".format(a.ndim))
print("a.shape    - {}".format(a.shape))
print("a.size     - {}".format(a.size))
print("a.dtype    - {}".format(a.dtype))
print("a.itemsize - {}".format(a.itemsize))
print("a.reshape  - {}".format(a.reshape(3,4)))

'''
a = np.identity(5)
print("a          - {}".format(a))
print("type(a)    - {}".format(type(a)))
print("a.ndim     - {}".format(a.ndim))
print("a.shape    - {}".format(a.shape))
print("a.size     - {}".format(a.size))
print("a.dtype    - {}".format(a.dtype))
print("a.itemsize - {}".format(a.itemsize))
'''
#a = np.full((4,2), 4.3, dtype='float16')
#print(a)

#print(np.random.rand(9))
#print(np.random.rand(2, 3))
#print(np.random.random_sample(5))

#print(np.random.randint(-5, 21, 30))
#print(np.random.randint(6, 21, (2,4)))

#print(np.identity(3))
#print(np.identity(4))


#a = np.random.rand(2,3)
#print(a)
#r = a.repeat(4, axis=0)     # axis == 0 - ROW
#print(r)
#r = a.repeat(4, axis=1)     # axis == 1 - COLUMN
#print(r)

# Exercise

onesArray = np.ones((5,5), dtype='int16')
print(onesArray)
z = np.zeros((3,3))
print(z)
z[1,1] = 8
print(z)
onesArray[1:4, 1:4] = z
print(onesArray)
