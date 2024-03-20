import numpy as np
import pandas as pd

df1 = pd.read_csv('C:/Users/User/Downloads/custom.txt', header=None)
df2 = pd.read_csv('C:/Users/User/Downloads/order.txt', header=None)

df1.columns = ['id', 'name', 'age', 'location', 'salary']
df2.columns = ['order_id', 'date_time', 'id', 'amount']

# name, age, location, date, amount
df3 = pd.merge(df1, df2, on='id', how='inner')[['name', 'age', 'location', 'date_time', 'amount']]
print(df3)

# name, location, salary, date, amount for salary>2000
df4 = pd.merge(df1, df2, on='id', how='inner')\
        .loc[df1['salary'] > 2000][['name', 'location', 'salary', 'date_time', 'amount']]
print(df4)

# age max 1 employee name, age, salary, date
df5 = pd.merge(df1, df2, on='id', how='inner')\
        .sort_values(by='age', ascending=False)[['name', 'age', 'salary', 'date_time']]\
        .head(1)
print(df5)

# latest date: name, age, location, date, amount
df6 = pd.merge(df1, df2, on='id', how='inner')\
        .sort_values(by='date_time', ascending=False)[['name', 'age', 'location', 'date_time', 'amount']]\
        .head(1)
print(df6)

# salary above 2000 and amount above 1000 print name, age, salary, amount
df7 = pd.merge(df1, df2, on='id', how='inner')\
        .loc[(df1['salary'] > 2000) & (df2['amount'] > 1000)][['name', 'age', 'salary', 'amount']]
print(df7)
