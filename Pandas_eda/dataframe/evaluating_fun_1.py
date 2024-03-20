import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/customer5.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'profession', 'location', 'salary']

# 1. Each profession count  [count desc]
df1 = df.groupby('profession')['profession'].count().sort_values(ascending=False)
print(df1)
print('*'*100)

# 2. Each profession total salary  [salary desc]
df2 = df.groupby('profession')['salary'].sum().sort_values(ascending=False)
print(df2)
print('*'*100)

# 3. Each country maximum salary
df3 = df.groupby('location')['salary'].max().sort_values()
print(df3)
print('*'*100)

# 4. Each profession min salary
df4 = df.groupby('profession')['salary'].min().sort_values()
print(df4)
print('*'*100)

# 5. Each country average salary
df5 = df.groupby('location')['salary'].mean().sort_values()
print(df5)
print('*'*100)

# 6. Each profession mean salary
df6 = df.groupby('profession')['salary'].mean().sort_values()
print(df6)
