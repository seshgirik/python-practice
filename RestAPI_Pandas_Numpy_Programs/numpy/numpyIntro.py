import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)


b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimension
a.ndim

# Get Shape
b.shape

# Get Type
a.dtype

# Get Size
a.itemsize

# Get number of elements
a.size

# Get total size
a.nbytes

print("==============================================")

###     Accessing/Changing specific elements, rows, columns, etc     ####

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
a[1, 5]

# Get a specific row
a[0, :]

# Get a specific column
a[:, 2]

# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:2]

a[1,5] = 20

a[:,2] = [1,2]
print(a)

#####    3-d example      #####
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

# Get specific element (work outside in)
b[0,1,1]

print("==============================================")

############### Initializing Different Types of Arrays ##################

# All 0s matrix
np.zeros((2,3))

# All 1s matrix
np.ones((4,2,2), dtype='int32')


# Any other number
np.full((2,2), 99)

# Any other number (full_like)
np.full_like(a, 4)

# Random decimal numbers
np.random.rand(4,2)

# Random Integer values
np.random.randint(-4,8, size=(3,3))