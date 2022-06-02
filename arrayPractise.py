from Numpy import *

arr = array([
    [1,2,3,4],
    [4,5,6,7]
])

print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.flatten())
print(arr.reshape(4,2))
print(arr.reshape(4,2,1))    # convert array into further small arrays with one value each

m = matrix('1,2,3,4,5;6,7,8,9,10')

print(m)
