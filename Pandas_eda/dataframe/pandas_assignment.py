import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/movies_cleaned_pandas.csv', header=None)
df.columns = ['id', 'movie_name', 'year', 'rating', 'duration']

# 1. Find row count
print(len(df))

# 2. Remove duplicates and find row count
df1 = df.drop_duplicates()
print(len(df1))

# 3. Sort dataset by release year in descending order
df2 = df.sort_values(by='year', ascending=False)
print(df2)

# 4. Find rating max 5 movies, name, year, rating
df3 = df.sort_values(by='rating', ascending=False)[['movie_name', 'year', 'rating']].head(5)
print(df3)

# 5. Find rating minimum 3 movies name,year,rating
df4 = df.sort_values(by='rating')[['movie_name', 'year', 'rating']].head(3)
print(df4)

# 6. Find Each year release movie count [count desc order]
df5 = df.groupby('year')['movie_name'].count().sort_values(ascending=False)
print(df5)

# 7. Each rating count [count desc order]
df6 = df.groupby('rating')['rating'].count().sort_values(ascending=False)
print(df6)

# 8. 2008 and rating above 3 [collect]
df7 = df.loc[(df['year'] == 2008) & (df['rating'] > 3.0)]
print(df7)
# A. row count
print(len(df7))

# 9. Find duration mxm 1 movies name,year,rating,duration
df8 = df.sort_values(by='duration', ascending=False)[['movie_name', 'year', 'rating', 'duration']].head(1)
print(df8)

# 10. Find rating mnm 1 movies name,year,rating,duration
df9 = df.sort_values(by='rating')[['movie_name', 'year', 'rating', 'duration']].head(1)
print(df9)

# 11. Rating above 4 and release year above 2005
# A. Rating mxm movies full data
df10_A = df.loc[(df['rating'] > 4.0) & (df['year'] > 2005)].sort_values(by='rating').tail(1)
print(df10_A)
# B. Rating mnm movies full data
df10_B = df.loc[(df['rating'] > 4.0) & (df['year'] > 2005)].sort_values(by='rating').head(1)
print(df10_B)

# 12. 2008 movies count
df11 = df.loc[df['year'] == 2008].groupby('year')['year'].count()
print(df11)

# 13. 1975-2000 movies collect
# A. Row count
df12 = df.loc[(df['year'] > 1975) & (df['year'] < 2000)]
print(df12)
print(len(df12))

# 14. 1975-2000 and rating above 3.5 total row count
df13 = df.loc[((df['year'] > 1975) & (df['year'] < 2000)) & (df['rating'] > 3.5)]
print(len(df13))
