import numpy as np
from scipy import linalg

# Create a vector as a row
vectorRow = np.array([1, 2, 3])
print(vectorRow)

# Create a vector as a column
vectorColumn = np.array([[1], [3], [6]])
print(vectorColumn)


# Vector multiplication
vector_a = np.array([[1, 4], [5, 6]])
vector_b = np.array([[4, 1], [2, 2]])
res = np.vdot(vector_a, vector_b)
print(res)

res = np.vdot(vector_b, vector_a)
print(res)

# Determinant of a Matrix
matrix1 = np.matrix([[1, 2],[3, 4]])
print(np.linalg.det(matrix1))

# Inverse of a Matrix
Y = np.array(([1,2], [3,4]))
Z = np.linalg.inv(Y)
print(Z)

# Trace of a Matrix - sum of all the elements in the diagonal of a matrix.
# 1+5+9=15
X = np.array(([1,2,3], [4,5,6], [7,8,9]))
Z = np.trace(X)
print(Z)

# Apply some function to each element of array/matrix.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix)

add_1000 = lambda i: i + 1000

# create vectorized function
vectorized_add = np.vectorize(add_1000)

# apply function to all elements in matrix
res = vectorized_add(matrix)
print(res)


# Transposing a Vector or Matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.T)

# Getting the Diagonal of a Matrix
print(matrix.diagonal())

# Arithmetic operation on matrices.
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

matrix_b = np.array([[1,3,5],
                     [2,3,1],
                     [1,3,8]])

np.add(matrix_a, matrix_b)          # matrix_a + matrix_b
np.subtract(matrix_a, matrix_b)     # matrix_a - matrix_b
np.dot(matrix_a, matrix_b)          # matrix_a @ matrix_b ( @ in python 3.5 for multiplication)


# Inverse of matrix
inverseMatrix = linalg.inv(matrix_b)
print("Inverse of matrix -- \n{}".format(inverseMatrix))


# Solving linear equation
# x+3y+5z=10
# 2x+3y+z=8
# x+3y+8z=3

# https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html

matrix_b = np.array([[1,3,5],
                     [2,3,1],
                     [1,3,8]])
B = np.array([[10], [8], [3]])
result = np.linalg.solve(matrix_b, B)
print("Solving linear equation ----\n{}".format(result))


# Find the eigenvalues and eigenvectors of a square matrix.
#eigenvalues, eigenvectors = np.linalg.eig(matrix)
#print(eigenvalues)
#print(eigenvectors)
