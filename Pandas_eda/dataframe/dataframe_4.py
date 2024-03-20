import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/movies_cleaned_pandas.csv', header=None)
df.columns = ['id', 'movie_name', 'year', 'rating', 'duration']
print(df)
