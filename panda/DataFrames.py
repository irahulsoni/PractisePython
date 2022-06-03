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

# While using multiple  conditions, use & not and , | for or
# dataFrame[  (First  condition) & (second condition) ]
print(df[(df['W']> 0 ) & (df['Y'] > 1)])

# Multi index
outside= ['G1','G1','G1','G2','G2','G2']
inside =[1,2,3,1,2,3]
hier_index = list(zip(outside, inside))

# creating multiple indexes
hier_index = pd.MultiIndex.from_tuples(hier_index)


dff = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(dff)

print(dff.loc['G1'].loc[1])

dff.index.names = ['Groups', 'Num']

print(dff)

print(dff.loc['G1'].loc[2]['B'])


d = {'A':[1,1.5,2],'B':[1,np.nan,3],'C':[5,np.nan,np.nan]}

dfff = pd.DataFrame(d)

print(dfff)

print(dfff.dropna())

#to keep atleast 1 nan value
print(dfff.dropna(thresh=2))

# to fill nan value with something
print(dfff.fillna('FIll Up'))

print(dfff.fillna(dfff['A'].mean()))
