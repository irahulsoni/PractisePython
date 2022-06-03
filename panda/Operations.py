import pandas as pd
import numpy as np

# for using sql
from sqlalchemy import create_engine

np.random.seed(101)
d = np.random.randint(1,10, [3, 3])
df = pd.DataFrame(data=d, index=['A', 'B', 'C'])
print(df)

#get unique values in column
print(df[1].unique())
# number of unique numbers:
print(df[1].nunique())

# number of unique values:
print(df[1].value_counts())


#Apply our own functions :
def times2(x):
    return x*2

print(df[1].apply(times2))

# rea filee:
#pd.read_csv("fileName.csv")

# make a csv

df.to_csv('Name',index=False)

# make excel file
#df.to_excel('nameExcel', sheet_name='Sheet')

# Sql
engine= create_engine('sqlite:///:memory:')

df.to_sql('my_table',engine)

sqldf = pd.read_sql('my_table',con =engine)
print(sqldf)
