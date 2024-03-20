# How to convert an external file to a dataframe
# if the file is a csv, we need not provide the separation argument as the function will separate the file contents
# based on comma by default
# check whether the file contains a header tag or not
# If not, include header=None as one of the arguments

import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/customer1.txt', sep=',', header=None)

# Add column names
df.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location']
print(df)

# iloc function: to collect rows in between the dataframe
df1 = df.iloc[3]
print(df1)

df2 = df.iloc[3:11]
print(df2)

df3 = df.iloc[::10]
print(df3)

# In most machine learning problems, the output and the input columns should be separated as x and y variables which can
# be done as follows,
# x contains all the columns except last column
# y contains only the last column where the output is predicted by the machine

x = df.iloc[:, :-1]
print(x)

y = df.iloc[:, -1]
print(y)

# how to collect columns without using iloc function
df3 = df[['first_name', 'last_name', 'location']]
print(df3)

# first 50 employee, print first name, last name, age, prof
df4 = df[['first_name', 'last_name', 'age', 'profession']].head(50)
print(df4)

# How to handle missing data
print(df.isna().sum())
# prints the number of missing values in each column

# to fill the missing values
# fillna() function
df5 = df.fillna('India')
print(df5.isna().sum())

# filter ==> loc function
# to collect the data that satisfy a particular function
# syntax:
# newdf = olddfname.loc[olddf['colname']condition]

# age above 50
df6 = df.loc[df['age'] > 50]
print(df6)

# location = India
df7 = df.loc[df['location'] == 'india']
print(df7)

# location=Us, print fname, lname, age, prof
df8 = df.loc[df['location'] == 'us'][['first_name', 'last_name', 'age', 'profession']]
print(df8)

# age>50 and location=India
# If more than one condition, syntax:
# df1=df.loc[(df['colname1']condition1)&(df['colname2']condition2)]
df9 = df.loc[(df['age'] > 50) & (df['location'] == 'india')]
print(df9)
