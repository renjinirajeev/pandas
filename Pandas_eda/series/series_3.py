import numpy as np
import pandas as pd

a = pd.Series([6, 2, 5, 8, 9, 4, 10, 15])
print(a)
print(a.dtype)

# head() function: returns first n values in a series(5 by default), returns first n rows in a dataframe(5 by default)
print(a.head())
print(a.head(7))
print(a.head(3))

# tail() function: returns last n values in a series(5 by default), returns last n rows in a dataframe(5 by default)
print(a.tail())
print(a.tail(2))
print(a.tail(6))

# shape()
print(a.shape)

