# Transaction file
# Columns:
#   Order Id
#   Purchase date
#   Customer Id
#   Amount paid
#   Category
#   Product
#   City
#   State
#   Payment method

import numpy as np
import pandas as pd
df = pd.read_csv('C:/Users/User/Downloads/txn.txt', header=None)
df.columns = ['id', 'date', 'customer_id', 'amount', 'category', 'product', 'city', 'state', 'payment_method']

# 1. Find Row count
print(len(df))
print('*'*100)

# 2. jan month oid,customer no,category,product,state
#  A. Row count
df1 = df.loc[(df['date'] >= '01-01-2011') & (df['date'] <= '01-31-2011')][['id', 'customer_id', 'product', 'state']]
print(df1)
print(len(df1))
print('*'*100)

# 3. July Month oid,customer no,category,product,state
#  B. Row count
df2 = df.loc[(df['date'] >= '07-01-2011') & (df['date'] <= '07-31-2011')][['id', 'customer_id', 'product', 'state']]
print(df2)
print(len(df2))
print('*'*100)

# 4. Each category [count desc sort]
df3 = df.groupby('category')['category'].count().sort_values(ascending=False)
print(df3)
print('*'*100)

# 5. Category full details
df4 = df.loc[df['category'] == 'Outdoor Recreation']
print(df4)
print('*'*100)

# 6. Each payment method count
df5 = df.groupby('payment_method')['payment_method'].count()
print(df5)
print('*'*100)

# 7.  jan-july month purchase count [include]
df6 = df.loc[(df['date'] >= '01-01-2011') & (df['date'] <= '07-31-2011')]
print(df6)
print(len(df6))
print('*'*100)

# 8. Each category total amount
df7 = df.groupby('category')['amount'].sum().sort_values()
print(df7)
print('*'*100)

# 9. Each category maximum amount
df8 = df.groupby('category')['amount'].max().sort_values()
print(df8)
print('*'*100)

# 10. Each category avg amount
df9 = df.groupby('category')['amount'].mean().sort_values()
print(df9)
print('*'*100)

# 11. total amount by cash and credit card
df10 = df.groupby('payment_method')['amount'].sum()
print(df10)
print('*'*100)

# 12. Indoor games ,total amount
df11 = df.loc[df['category'] == 'Indoor Games'].groupby('category')['amount'].sum()
print(df11)
print('*'*100)

# 13. Each state count
df12 = df.groupby('state')['state'].count().sort_values()
print(df12)
print('*'*100)
