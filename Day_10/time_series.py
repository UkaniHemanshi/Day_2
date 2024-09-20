# creating time series with random data
import numpy as np
import pandas as pd
start_date ='2024-01-01'
end_date = '2024-01-10'
dates = pd.date_range(start=start_date,end= end_date)

data = np.random.randn(10)
time_series = pd.Series(data,index=dates)
print(time_series)

# accesing data for a specific date
print("time series for:'2024-01-05'",time_series['2024-01-05'])

# accesing data withing a date range
print("Time series for range:\n",time_series['2024-01-03':'2024-01-06'])

# boolean indexing to select dates based on a condition
print("With boolean indexing:\n",time_series[time_series>0])

# create a time series with hourly frequency
hourly_dates = pd.date_range(start='2024-01-01',periods=24,freq='h')
hourly_data = np.random.randn(24)
hourly_series = pd.Series(hourly_data,index=hourly_dates)
print("complete hourly series\n",hourly_series)

# accessing data for a specific hour
print("hourly series:",hourly_series['2024-01-01 15:00'])

# selecting data within a range and with a condition
print("Data with multiple conditions:\n",time_series['2024-01-01':'2024-01-10'][time_series>0])

# access data for a specific date
print(time_series.loc['2024-01-05'])

# access data within date range
print(time_series.loc['2024-01-03':'2024-01-06'])

# access data for multiple specific dates
print("multiple specific dates:\n",time_series.loc[['2024-01-01','2024-01-05','2024-01-10']])

# access data for the first element(position 0)
print(time_series.iloc[0])

# access data for positions from 2 to 5
print(time_series.iloc[2:6])

# access data for specific positions
print(time_series.iloc[[0,3,7]])

# slicing data within a date range
print(time_series['2024-01-03':'2024-01-06'])

# access data before a specific date
print(time_series[:'2024-01-05'])

# access data after a specific date
print(time_series['2024-01-06'])

