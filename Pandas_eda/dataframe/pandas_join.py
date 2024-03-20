# Pandas joining
# combining two dataframes
# 4 types of joining
# 1. Inner joining
# 2. Left-outer joining
# 3. Right-outer joining
# 4. full-outer joining

# inner joining is the most frequently used

import numpy as np
import pandas as pd

dict_1 = {'id': [1, 2, 3, 4, 5],
          'fname': ['Vinay', 'Prasanth', 'Prateesh', 'Vinod', 'Suraj'],
          'lname': ['K', 'P', 'V', 'A', 'T'], 'age': [24, 26, 28, 27, 25]}
dict_2 = {'id': [4, 5, 6, 7, 8],
          'prof': ['Data Science', 'Python', 'Big data', 'Testing', 'Asp.net'],
          'location': ['kochi', 'calicut', 'thrissur', 'trivandrum', 'kochi'],
          'salary': [25000, 10000, 24000, 15000, 20000]}

df1 = pd.DataFrame(dict_1)
df2 = pd.DataFrame(dict_2)
print(df1)
print(df2)

# 1. Inner joining
# The two dataframes are joined using a common field. Only those values present in the common field of both the columns
# are combined after the operation.

# In the above case, the field, 'id' is common in both dataframes.
# the ids 4 and 5 and the corresponding data from each dataframe are printed as those are the only ids that are equal
# in both the dataframes.

# syntax:
# newdfname = pd.merge(dataframe1, dataframe2, on='common_field_name', how='inner')

df3 = pd.merge(df1, df2, on='id', how='inner')
print(df3)

# print fname, lname, age, salary of those whose salary>13000
df4 = pd.merge(df1, df2, on='id', how='inner')\
        .loc[df2['salary'] > 13000][['fname', 'lname', 'age', 'salary']]
print(df4)

# print fname, lname, prof, salary of one employee with max age
df5 = pd.merge(df1, df2, on='id', how='inner')\
        .sort_values(by='age', ascending=False)[['fname', 'lname', 'prof', 'salary']]\
        .head(1)
print(df5)

# **********************************************************************************************************************

# 2. Left outer joining
# returns all the row from left dataframe(first df) as well as matching values from right dataframe or null(NaN) in case
# of no matching values.

# syntax:
# newdfname = pd.merge(dataframe1, dataframe2, on='common_field_name', how='left')

df6 = pd.merge(df1, df2, on='id', how='left')
print(df6)

# **********************************************************************************************************************

# 2. Right outer joining
# returns all the row from right dataframe(second df) as well as matching values from left dataframe or null(NaN)
# in case of no matching values.

# syntax:
# newdfname = pd.merge(dataframe1, dataframe2, on='common_field_name', how='right')

df7 = pd.merge(df1, df2, on='id', how='right')
print(df7)

# **********************************************************************************************************************

# 2. Full outer joining
# returns the combined result of left and right outer joining.

# syntax:
# newdfname = pd.merge(dataframe1, dataframe2, on='common_field_name', how='outer')

df8 = pd.merge(df1, df2, on='id', how='outer')
print(df8)
