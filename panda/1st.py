#Series
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]

arr = np.array(my_data)

d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data = my_data))
print(pd.Series(data = my_data, index = labels))  # or print(pd.Series(my_data, labels))

# can use anything but in same format pd.Series(data, index)
# with arrays
print(pd.Series(arr, labels))

ser1 = pd.Series([1,2,3,4],['India','Canada','USA','UK'])
# Returns the value at particular index
print(ser1['USA'])

