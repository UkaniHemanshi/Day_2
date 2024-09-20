import pandas as pd

# creating a series
data = pd.Series([10,20,20,30,40])

#rankig with different methods
print("Average rank:")
print(data.rank(method='average'))

print('\nMin rank:')
print(data.rank(method='min'))

print('\nMax rank:')
print(data.rank(method='max'))

print('\nFirst rank:')
print(data.rank(method='first'))

print('\nDense rank:')
print(data.rank(method='dense'))
