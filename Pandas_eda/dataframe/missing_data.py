# Missing value handling

import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/missing_data1.csv')
# print(df)

# If we use fillna function along with the argument inplace, we get the missing places filled in the same df
# without creating a new df
# df.fillna(200, inplace=True)
# print(df.isna().sum())

# to fill a particular column
# df['Calories'].fillna(275, inplace=True)
# print(df)
#
# df['Date'].fillna('2024/01/30', inplace=True)
# print(df)

# **********************************************************************************************************************

# Handling missing values logically using:
# mean(used in case of numerical values)
# median(used in case of both numerical and object values)
# mode(used mostly in case of object values)

# filling missing values in calories field using mean
# x = df['Calories'].mean()
# df['Calories'].fillna(x, inplace=True)
# print(df)

# filling missing values in calories field using median
# y = df['Calories'].median()
# df['Calories'].fillna(y, inplace=True)
# print(df)

# filling missing values in calories field using mode
# z = df['Calories'].mode()[0]
# df['Calories'].fillna(z, inplace=True)

# filling missing value in date field using mode
# p = df['Date'].mode()[0]
# df['Date'].fillna(p, inplace=True)
# print(df)

# **********************************************************************************************************************

# To drop the rows with missing values, we use dropna() function
df.dropna(inplace=True, ignore_index=True)
# print(df)

# To drop only particular rows having missing values
# df.dropna(subset=['Date'], inplace=True, ignore_index=True)
# print(df)

# **********************************************************************************************************************

# How to handle data with wrong format
# data that doesn't match logically. For example, in this file, the duration ranges from 30 to 60
# except the value in index 7
# dfname.loc[wrong_format_index, colname] = value (we can fill using mean or median or mode as well)

df.loc[7, 'Duration'] = 50
# print(df)

# If we need to change all values greater than 400 in calories field, to mean,
q = df['Calories'].mean()
for i in df.index:
    if df.loc[i, 'Calories'] > 400:
        df.loc[i, 'Calories'] = q
print(df)
