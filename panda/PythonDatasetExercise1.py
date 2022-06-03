import numpy as np
import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv('/Users/admin/Desktop/Study/Python/PractisePython/data/Salaries.csv')

# total columns we have
print(data.head())

#total entries we have
print(data.info())

#looking for something specific
#print(data['BasePay'].mean())

# get info out of the table

print(data[data['EmployeeName'] == 'GARY JIMENEZ']['JobTitle'])

#TOTAL SALARIES INCLUDING BENIFITS

print(data[data['EmployeeName'] == 'GARY JIMENEZ'][['TotalPay'] + ['Benefits']])

# name of highest paid person
print(data[data['TotalPayBenefits'].max() == data['TotalPayBenefits']]['EmployeeName'])

# or

print(data.loc[data['TotalPayBenefits'].idxmax()]['EmployeeName'])


print(data[data['Year'] == 2013]['JobTitle'].value_counts() == 1)
