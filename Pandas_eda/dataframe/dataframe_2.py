import numpy as np
import pandas as pd

dict_1 = {'id': [101, 102, 103, 104, 105],
          'first_name': ['Vinay', 'Arjun', 'Amal', 'Vineet', 'Vivek'],
          'last_name': ['K', 'V', 'R', 'S', 'T'],
          'age': [28, 23, 24, 26, 22],
          'course': ['Python', 'Data Science', 'Bigdata', 'Software testing', 'Data Science'],
          'location': ['Kochi', 'Calicut', 'Trivandrum', 'Kochi', 'Calicut']}

df = pd.DataFrame(dict_1)
print(df)
print(df.describe())
print(df.describe(include='O'))
print(df.describe(include='all'))
