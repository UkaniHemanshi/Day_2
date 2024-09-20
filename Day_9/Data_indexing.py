import pandas as pd
import numpy as np

data = {"Name":['Alice','Bob','Charlie'],"Age":[23,34,35],'City':['newyork','mathura','surat']}
df = pd.DataFrame(data)
print(df)
print()

print(df.iloc[0])
print()
print(df.iloc[:2])
print()
print(df.iloc[1:3,[0,1]])
print()
print(df.loc[1])
print()
print(df.loc[df['Age']>30])