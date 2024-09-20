import pandas as pd

#sample data
data = {'values':[10,12,12,13,12,14,10,13,13,400]}
df = pd.DataFrame(data)

#calculate Q1 Q3 ad IQR
Q1 = df['values'].quantile(0.25)
print("Q1:",Q1)
Q3 = df['values'].quantile(0.75)
print("Q3:",Q3)
IQR = Q3-Q1
print("IQR:",IQR)

#define bounds for outliers
lower_bound = Q1 - 1.5 *IQR
upper_bound = Q3 + 1.5 *IQR

print("lower_bound:",lower_bound)
print("upper_bound:",upper_bound)

#Identify outliers
outliers = df[(df['values']<lower_bound) | (df['values']>upper_bound)]
print("outliers:\n",outliers)