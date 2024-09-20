import pandas as pd
import numpy as np

#creating data frame from dictionary
data = {"Name":['Alice','Bob','Charlie'],"Age":[23,34,35],'City':['newyork','mathura','surat']}
df = pd.DataFrame(data)
print(df)
print()

#creating a data frame froam a list

names=['alice','bob','charlie']
age=[23,34,45]
City=['newyork','mathura','surat']
df=pd.DataFrame({'Name':names,'Age':age,'city':City})
print(df)
print()


#creating a dataframe from Numpy array
array = np.array([[25,'Newyork'],[30,'India'],[40,'Canada']])
df=pd.DataFrame(array, columns=['Age','City'])
print(df)
print()


#Reading a Dataframe from a csv file
df = pd.read_csv('DataDemo.csv')
print(df)
print()

#creating a dataframe from series
names=pd.Series(['Alice','Bob','charlie'],name='Name')
ages=pd.Series([25,36,45],name='Age')
df = pd.concat([names,ages],axis=1)
print(df)


