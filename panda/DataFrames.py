import numpy as np
import pandas as pd

from numpy.random import randn

# seed so we have same random number all the time
np.random.seed(101)

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
#putting axis = 1 drops the column, by default axis = o which mean index value, inplace to make changes to happen

df.drop('new',axis=1, inplace= True)

# to select the rows: we use loc function, known as locate

df.loc['A']

#or iloc : Using index as numerical base
df.iloc[2]

# making a boolean data frame
booldf = df > 0

print(booldf)

#only shows values that are greater than 0

print(df[df > 0])

# will remove the null values and give rows with true in boolean in column W
print(df[df['W'] > 0])

# display rows having value greater than 0 in columns X, Y
            # Rows    # columns
print(df[df['W']>0][['X','Y']])

# While using multiple  conditions, use & not and
# dataFrame[  (First  condition) & (second condition) ]
print(df[(df['W']> 0 ) & (df['Y'] > 1)])
