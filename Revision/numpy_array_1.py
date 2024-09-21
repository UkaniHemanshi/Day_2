import numpy as np

sales = np.array([5,4,8,22,45,37,88,90,2,34])

print("Sales for 5th day",sales[4])

first_five_days = sales[:5]
print("sales data for first five days:",first_five_days)

last_three_days = sales[-3:]
print("sales data for last three days:",last_three_days)

new_sales = sales +10
print(new_sales)

price = 2000

discounted_sales = (sales*price*10)/100
print(discounted_sales)

