import numpy as np
import pandas as pd

a = pd.Series([5, 8, 9, 4, 10, 15], index=[1, 5, 0, 4, 2, 3])
print(a)

# the index and the corresponding elements are printed by default. But, we can define an order for the index according
# to our wish but it does not affect the order of values
