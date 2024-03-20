import numpy as np
import pandas as pd

lst = [[101, 'Vinay', 'K', 29, 'Bigdata', 10000, 'Ernakulam'],
       [102, 'Arjun', 'P', 30, 'Python', 18000, 'Calicut'],
       [103, 'Amal', 'Q', 27, 'Bigdata', 20000, 'Trivandrum'],
       [103, 'Amal', 'Q', 27, 'Bigdata', 20000, 'Trivandrum'],
       [104, 'Vineet', 'P', 31, 'Testing', 25000, 'Kochi'],
       [105, 'Vivek', 'Q', 31, 'Testing', 20000, 'Calicut'],
       [106, 'Suraj', 'S', 30, 'Python', 18000, 'Thrissur'],
       [107, 'Abhinand', 'R', 29, 'Bigdata', 28000, 'Trivandrum']]
df = pd.DataFrame(lst, columns=['id', 'first_name', 'last_name', 'age', 'profession', 'salary', 'location'])
print(df)
print(df.shape)
print(df.head(2))
print(df.tail(2))
print(df.dtypes)
# dtype function prints the column names and the corresponding data types.
# The string data type in pandas is called object

# describe() function
# describe function works for columns with integer data types only
print(df.describe())

# If I want to describe the object data type columns,
print(df.describe(include='O'))

# If I want to describe the whole data,
print(df.describe(include='all'))

# How to add new column into a dataframe
df['Gender'] = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']
print(df)

# How to delete a column from the dataframe
df1 = df.drop(['profession'], axis=1)
print(df1)

# How to rename a column
df2 = df.rename(columns={'first_name': 'fname'})
print(df2)

# How to collect unique rows/ how to remove duplicate rows
# drop_duplicates()
df3 = df.drop_duplicates()
print(df3)
