import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/customer1.txt', sep=',', header=None)

# Add column names
df.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location']

# Evaluating functions
# before using any evaluating functions, we must use groupby() function

# COUNT(): To find the count corresponding to each column in a dataframe
# newdfname = olddfname.groupby('colname') ['colname'].count()
# find the profession count and sort in ascending order
df1 = df.groupby('profession')['profession'].count()\
        .sort_values()  # default sort by count in the ascending order. give ascending=0 for descending order.
print(df1)
print('*'*100)

# find the location count and sort in descending order
df2 = df.groupby('location')['location'].count()\
        .sort_values(ascending=False)
print(df2)
print('*'*100)

# profession count of those who work in India
df3 = df.loc[df['location'] == 'india']\
        .groupby('profession')['profession'].count()\
        .sort_values(ascending=False)
print(df3)

# **********************************************************************************************************************

# MAX(): to find the maximum of a column relating to another column. Eg: to find the maximum salary in each profession
# syntax:
# newdfname = olddfname.groupby('colname1') ['colname2'].max()
# Find the maximum age for people working in each profession
df4 = df.groupby('profession')['age'].max()
print(df4)

df5 = pd.read_csv('C:/Users/User/Downloads/Temperature.unknown', sep=' ', header=None)
df5.columns = ['year', 'temperature']
df6 = df5.groupby('year')['temperature'].max()
print(df6)
df7 = df5.groupby('year')['temperature'].max().sort_values(ascending=False)
print(df7)

# **********************************************************************************************************************

# MIN(): to find the minimum of a column relating to another column. Eg: to find the minimum salary in each profession
# # syntax:
# newdfname = olddfname.groupby('colname1') ['colname2'].min()
df8 = df5.groupby('year')['temperature'].min().sort_values()
print(df8)

# **********************************************************************************************************************

# SUM(): calculates the sum of a column corresponding to another column. Eg: total temperature in a particular year.
# syntax:
# newdfname = olddfname.groupby('colname1') ['colname2'].sum()
df9 = df5.groupby('year')['temperature'].sum().sort_values()
print(df9)

# **********************************************************************************************************************

# MEAN(): calculates the average of a column corresponding to another column. Eg: average temperature in a
#         particular year.
df10 = df5.groupby('year')['temperature'].mean().sort_values()
print(df10)
