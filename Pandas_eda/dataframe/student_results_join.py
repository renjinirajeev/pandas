import numpy as np
import pandas as pd

df1 = pd.read_csv('C:/Users/User/Downloads/student.unknown', header=None)
df2 = pd.read_csv('C:/Users/User/Downloads/results.unknown', header=None)

df1.columns = ['name', 'roll_no']
df2.columns = ['roll_no', 'result']

df3 = pd.merge(df1, df2, on='roll_no', how='inner')\
        .loc[df2['result'] == 'pass'][['roll_no', 'name', 'result']]
print(df3)
