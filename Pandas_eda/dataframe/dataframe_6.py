import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/sample4.txt', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'ph.no.', 'location']
print(df)

# age = 22, print fname, lname, age, ph.no.
df1 = df.loc[df['age'] == 22][['fname', 'lname', 'age', 'ph.no.']]
print(df1)

# location = chennai, print fname, lname, age, ph.no.
df2 = df.loc[df['location'] == 'Chennai'][['fname', 'lname', 'age', 'ph.no.']]
print(df2)

# age=23 and location=chennai, print fname, lname, age, ph.no.
df3 = df.loc[(df['location'] == 'Chennai') & (df['age'] > 23)][['fname', 'lname', 'age', 'ph.no.']]
print(df3)

# sort: sort_values() function
# can sort in ascending or descending order(by default, ascending order). Give ascending=False as argument
# for sorting in descending order

# syntax
# newdf = olddfname.sort_values(by='colname')
df4 = df.sort_values(by='age', ascending=False)

# age max 1 employee, fname, lname, age
print(df4[['fname', 'lname', 'age']].head(1))

# age min 2 employee, fname, lname, age
print(df4[['fname', 'lname', 'age']].tail(2))

# chennai location age max 1 employee, fname, lname, age
df5 = df.loc[df['location'] == 'Chennai']\
        .sort_values(by='age', ascending=False)[['fname', 'lname', 'age']]\
        .head(1)
print(df5)

# when we need to use functions in pandas, prioritize acc. to the following order
# loc
# sort
# column
# head/tail
