import numpy as np

my_list = [1,2,3,4]

print(np.array(my_list))

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

# Quickly generating an array without creating one:
#use arrange methord. give start, stop, skip if any
print(np.arange(0, 10, 2))

# generate specific typer of arrays:
#like all zeros:

print(np.zeros(3))
# rows and collumns done using tuples:
print(np.zeros((5,5)))


#linspace same as arrange needs start, stop, skip if any, it gives evenly spaced points

print(np.linspace(0,5, 10))

# identity matrix, it has same number of rows and collumns with diagnols on 1s. It must be square all the time

print(np.eye(4))

#Random number

# gives arrays of random numbers with uniform distribution from 0 to 1
np.random.rand(5,5)

# any random number
np.random.randn(5,5)

# random 10 integers from 1 to 100
print(np.random.randint(1,100,10))

# reshape an array:
# number of rows * number of columns should be equal to th e length of the array

arr = np.arange(25)
arr.reshape(5,5)

# to find min or max value just use min or max
arr.max()

#to get the index number use argman or argmin

arr.argmax()
