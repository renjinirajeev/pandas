import numpy as np
import pandas as pd

a = {'id': 101, 'fname': 'Vinay', 'lname': 'K', 'age': 29, 'prof': 'Bigdata', 'salary': 10000}
series_1 = pd.Series(a, index=['fname', 'lname', 'id', 'prof', 'age', 'salary'])
print(series_1)

# Here, in case of dictionary, keys act as index when converted to series
