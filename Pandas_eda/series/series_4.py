import numpy as np
import pandas as pd

series_1 = pd.Series([6, 2, 5, 8, 9, 4, 10, 15])
print(series_1)
series_2 = pd.Series([4, 9, 5, 3, 7, 10, 9, 5])
print(series_2)

# append function: to combine two series, use ignore_index argument to append the index as well
c = series_1._append(series_2, ignore_index=True)
print(c)

# add two series
print(series_1.add(series_2))

# subtract two series
print(series_1.subtract(series_2))

# multiply two series
print(series_1.multiply(series_2))

# divide two series
print(series_1.divide(series_2))

# If the shape of the two series is not the same, then, an extra element called Nan==> Not a number will be present
# after the operation is performed
