import pandas as pd

df=pd.read_csv('Student_Data.csv')
print(dict(df))
print()
print(df.head())
print()
print(df.head(7))
print()
print(df.tail())
print()
print(df.info())
print()
print(df.describe())