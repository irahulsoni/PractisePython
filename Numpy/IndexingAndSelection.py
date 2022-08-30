import numpy as np

arr = np.arange(0, 11)

print(arr[1:5])
print(arr[:6])

# change first 6 indexes to 100
arr[:6] = 100

# to copy an array to make a new array

arr1 = arr.copy()

print(arr1)

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d.shape)
print(arr_2d[0][1])


# slice notation, grab only few of the elements from array:
# array_name[rows , columns]
print(arr_2d[:2, 1:])

arr2 = np.arange(0, 11)
# making a boolean array
print(arr2 > 5)
bool_arr = arr2 > 5

# getting the places where boolean turns out true
print(arr[bool_arr])

# or
print(arr2[arr2 < 3])

arr3 = np.arange(50).reshape(5,10)

print(arr3[1:3, 4:7])
