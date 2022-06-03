import numpy as np
import pandas as pd

data = {'Company': ['Goog', 'Goog', 'MSFT','MSFT', 'FB','FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

GroupbyCompany = df.groupby('Company')
print(GroupbyCompany.mean())
print(GroupbyCompany.sum())
print(GroupbyCompany.std())  # standard deviasion

print(GroupbyCompany.sum().loc['FB'])  # total sales of fb
print(GroupbyCompany.count())
print(GroupbyCompany.max())


print(GroupbyCompany.describe())
print(GroupbyCompany.describe().transpose()['FB'])
