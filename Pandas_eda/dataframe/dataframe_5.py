# Convert the file to dataframe
import numpy as np
import pandas as pd
df = pd.read_csv('C:/Users/User/Downloads/missing_data1.csv', sep=',')
print(df)

# find the data type
print(df.dtypes)

# print first 10 rows
print(df.head(10))

# total missing values
print(df.isna().sum())

# fill the missing values
df1 = df.fillna(200)
print(df1)
print(df1.isna().sum())
