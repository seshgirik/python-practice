import numpy as np
import pandas as pd

data = [(20, 1), (61, 45), (19, 15)]

#for i in data:
#    print(type(i), i)


arr = np.array(data)
print ("numpy array : \n{0}".format(arr))
print ("Type  of numPy array : {}".format(type(arr)))
print ("Shape of numPy array : {}".format(arr.shape))
print ("Dimension  of numPy array : {}".format(arr.ndim))
print(arr.itemsize)
print(arr.size)

print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.std())
print(arr.var())

'''
# Reshaped numpy array another way
brr = arr.reshape(2, 3)
print ("Reshaped numpy array using reshape : \n{0}".format(brr))
print ("Shape of numPy array : {}".format(brr.shape))

# Resized numpy array
arr.shape = (3,2)
print ("Resized numpy array : \n{0}".format(arr))
print ("Shape of numPy array : {}".format(arr.shape))

print ("itemsize of numPy array : {}".format(arr.itemsize))

emptyArr = np.empty([4, 4])
print ("Empty numPy array : \n{}".format(emptyArr))
print ("Shape of Empty numPy array : {}".format(emptyArr.shape))

zeroArr = np.zeros([3, 3])
print ("Zero numPy array : \n{}".format(zeroArr))
print ("Shape of Zero numPy array : {}".format(zeroArr.shape))

onesArr = np.ones([5, 5])
print ("Ones numPy array : \n{}".format(onesArr))
print ("Shape of Ones numPy array : {}".format(onesArr.shape))

# Joining of two numpy array using concatenate() method
a = np.array([[19, 18 , 17], [3, 2, 1], [6, 5, 4]])
b = np.array([[1, 2, 3], [4, 5,6 ], [7, 8, 9]])
concatArr = np.concatenate((a, b), axis = 0) # Join second array in column fashion
print ("Joining of two numpy array using concatenate based on axis == 0 : \n{}".format(concatArr))
concatArr = np.concatenate((a, b), axis = 1) # Join second array in row fashion
print ("Joining of two numpy array using concatenate based on axis == 1 : \n{}".format(concatArr))

# Joining of two numpy array using stack() method
stackJoiningArr = np.stack((a, b), axis = 0) # Join second array in column fashion
print ("Joining of two numpy array using stack based on axis == 0 : \n{}".format(stackJoiningArr))
stackJoiningArr = np.stack((a, b), axis = 1) # Join second array in row fashion
print ("Joining of two numpy array using stack based on axis == 1 : \n{}".format(stackJoiningArr))

# Joining of two numpy array using hstack() method in sequence horizontally (column wise)
a = np.array([[19, 18 , 17], [3, 2, 1], [6, 5, 4]])
b = np.array([[1, 2, 3], [4, 5,6 ], [7, 8, 9]])
hstackArr = np.hstack((a, b))
print ("Joining of two numpy array using hstack : \n{}".format(hstackArr))

# Joining of two numpy array using vstack() method in sequence horizontally (row wise)
a = np.array([[19, 18 , 17], [3, 2, 1], [6, 5, 4]])
b = np.array([[1, 2, 3], [4, 5,6 ], [7, 8, 9]])
vstackArr = np.vstack((a, b))
print ("Joining of two numpy array using vstack : \n{}".format(vstackArr))

# Splitting numpy array using split() - array split does not result in an equal division
a = np.array([[19, 18 , 17], [3, 2, 1], [6, 5, 4]])
b = np.split(a, 3)
print ("Original numpy array  : \n{}".format(a))
print ("Splitting numpy array using split : \n{}".format(b))


# Splitting numpy array using split() - array split does not result in an equal division
a = np.array([[19, 18 , 17, 16], [4, 3, 2, 1], [8, 7, 6, 5], [11, 12 ,13 ,14], [31, 32 ,33 ,34]])
b = np.split(a, 5)
print ("Original numpy array  : \n{}".format(a))
print ("Splitting numpy array using split : \n{}".format(b))


# Flatten vs ravel
print("----Flattening----")
arr2 = np.array([[1, 2, 3], [6, 8, 9], [4, 6, 3]])
print(arr2)
b1 = arr2.flatten()
print(b1)
b1[0] = 100
print(b1)
print(arr2)

print("----Ravel----")
arr2 = np.array([[1, 2, 3], [6, 8, 9], [4, 6, 3]])
print(arr2)
b1 = arr2.ravel()
print(b1)
b1[0] = 100
print(b1)
print(arr2)
'''