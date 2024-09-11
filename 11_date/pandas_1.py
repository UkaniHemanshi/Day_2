import pandas as pd

#creating a series from a list
data = [10,20,30,40,]
series = pd.Series(data)
print(series)
#sum of series
print(series.sum())

#FILTERING VALUES GREATER THAN 20

print('GREATER than 20', series[series>20])

#creating a series with a custom index
series = pd.Series(data, index=['a','b','c','d'])
print(series)

#creating a series from dictionary

data_dict = {'apple':1,'banana':5,'cherry':7}
series= pd.Series(data_dict)
print(series)

#creating a series from scalar value
series= pd.Series(10, index=['a','b','c'])
print(series)

#accesing element by index
print(series['b'])

#accesing elements by index
# print(series[1])

