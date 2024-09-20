import pandas as pd

df = pd.read_csv('customers.csv')
#display first 5 records
print(df.head())
#display customer id and country columns first 10 rows
print(df[['Customer Id','Country']].head(10))
#FILTER DATA BY CONDITION
print(df[(df['First Name'] =='Sheryl') &  (df['Country'] == 'United States of America')].head(5))
print(df.iloc[1:6,1:4])
print(df.loc[5:11, ['First Name', 'Last Name','Company','City']])




