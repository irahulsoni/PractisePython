import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2','A9'],
                    'B': ['B0', 'B1', 'B2','B9'],
                    'C': ['C0', 'C1',' C2','C9'],
                    'Key': ['K0', 'K1', 'K2','K3']},
                   index=[0, 1, 2, 'Key'])

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5','A10'],
                    'B': ['B3', 'B4', 'B5','b'],
                    'C': ['C3', 'C4',' C5','c'],
                    'Key': ['K0', 'K1', 'K2','K3']},
                   index=[3, 4, 5, 'Key'])

df3 = pd.DataFrame({'A': ['A6', 'A7', 'A8','a'],
                    'B': ['B6', 'B7', 'B8','b'],
                    'C': ['C6', 'C7', 'C8','c'],
                    'Key': ['K0', 'K1', 'K2', 'K3']},
                   index=[6, 7, 8, 'Key'])

#concatenation:  Always work with same dimensions, axis= 0 merges rows, axis = 1 merges collumns
concat = pd.concat([df1, df2, df3], axis=0)
print(concat)

#merge:
merg = pd.merge(df1, df2, how='outer', on=['Key'])

print(merg)

#Join:
df1.join(df2)
