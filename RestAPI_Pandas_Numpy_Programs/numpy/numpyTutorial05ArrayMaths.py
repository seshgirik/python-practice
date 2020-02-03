import numpy as np

a = np.array([3,2,8,16])
b = np.array([1,3,3,2])
print(a*2)
print(a**2)
print(a+22)
print(a-220)
print(a[a<10])
print(np.cos(a))
print(np.sin(a))
print(np.add(a, b))
print(np.multiply(a, b))
print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))
print(np.conjugate(np.array([3+3j,2+4j,8+6j,16+2j])))


#print(np.arange(0,20).reshape(4,5))
#print(np.arange(3, 30))

# Array multiplication
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
res = np.dot(a, b)
print(type(res))
print(res)

res = np.inner(a,b)
print(type(res))
print(res)

#[1 2               [11 12
# 3 4]               13 14]

#With dot():
#[1∗11+2∗13 3∗11+4∗13
# 1∗12+2∗14 3∗12+4∗14] = [37 40
#                         85 92]

#With inner():
#[1∗11+2∗12 1∗13+2∗14
# 3∗11+4∗12 3∗13+4∗14] = [35 41
#                         81 95]

res = np.matmul(a, b)
print(type(res))
print(res)