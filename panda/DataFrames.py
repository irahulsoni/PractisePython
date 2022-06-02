import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(100)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# to print more than one column we have to call the list of column indexes we want to peint
# When asked for single column we get back a series
# but when asked for multiple, we get back a dataframe
print(df[['W', 'Z']])

#Creating a new column
df['new'] = df['W'] + df['Y']
print(df['new'])

#deleting the column
#putting axis = 1 drops the column, by default axis = o which mean index value

df.drop('new',axis=1)
