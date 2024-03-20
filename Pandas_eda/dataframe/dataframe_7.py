import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/customer1.txt', sep=',', header=None)
df.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location']
print(df)
print('*'*100)

# Age max 10 employee, fname, lname, age, prof, loc
df1 = df.sort_values(by='age')[['first_name', 'last_name', 'age', 'profession', 'location']].tail(10)
print(df1)
print('*'*100)

# Age min 5 employee fname, lname, age, prof, location
df2 = df.sort_values(by='age')[['first_name', 'last_name', 'age', 'profession', 'location']].head(5)
print(df2)
print('*'*100)

# India work, age max 3 employee fname, lname, age, prof
df3 = df.loc[df['location'] == 'india'].sort_values(by='age')[['first_name', 'last_name', 'age', 'profession']].tail(3)
print(df3)
print('*'*100)

# Doctor profession, fname, lname, age
df4 = df.loc[df['profession'] == 'Doctor'][['first_name', 'last_name', 'age']]
print(df4)
print('*'*100)

# india location and prof doctor, fname, lname, age
df5 = df.loc[(df['profession'] == 'Doctor') & (df['location'] == 'india')][['first_name', 'last_name', 'age']]
print(df5)
print('*'*100)

# uk and age range 40 to 70, fname, lname, age
df6 = df.loc[(df['location'] == 'uk') & (df['age'] > 40) & (df['age'] < 70)][['first_name', 'last_name', 'age']]
print(df6)
print('*'*100)

# Pilot prof work, age mxm 2 employee fname,lname,age
df7 = df.loc[df['profession'] == 'Pilot'].sort_values(by='age')[['first_name', 'last_name', 'age']].tail(2)
print(df7)
print('*'*100)

# us, age minimum 3 employee fname,lname,age,prof
df8 = df.loc[df['location'] == 'us'].sort_values(by='age')[['first_name', 'last_name', 'age', 'profession']].head(3)
print(df8)
print('*'*100)

# Doctor prof age mxm 1 employee full data
df9 = df.loc[df['profession'] == 'Doctor'].sort_values(by='age').tail(1)
print(df9)
print('*'*100)

#  india and prof Doctor age minimum 1 employee full data
df10 = df.loc[(df['profession'] == 'Doctor') & (df['location'] == 'india')].sort_values(by='age').head(1)
print(df10)
