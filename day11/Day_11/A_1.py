import matplotlib.pyplot as plt
import numpy as np

list_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_data = np.random.randint(50, 500, size=12)


# Calculate average sales for each month
average_sales = np.mean(sales_data)


# Line plot
plt.figure(figsize=(8, 6))
plt.plot(list_month, sales_data, label='Sales Data', color='Blue', marker='o', linestyle='--')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

#bar chart
plt.figure(figsize=(8,6))
plt.bar(list_month,sales_data,color='purple')
plt.title('Bar Chart ')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()

#piechart
plt.figure(figsize=(8, 6))
plt.pie(sales_data, labels=list_month, autopct='%1.1f%%', startangle=140)
plt.title('Average Sales for Each Month')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


#-------------------------------------------------------------------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Sample data: 12 months of sales data for 5 products
# np.random.seed(0)  # For reproducibility
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
# sales_data = np.random.randint(50, 500, size=(12, 5))
#
# # Calculate average sales for each product
# average_sales = np.mean(sales_data, axis=0)
#
# # Line plot for each product
# plt.figure(figsize=(10, 6))
# for i, product in enumerate(products):
#     plt.plot(months, sales_data[:, i], label=product, marker='o', linestyle='--')
# plt.title('Monthly Sales Data for Each Product')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.legend()
# plt.grid(True)
# plt.show()
#
# # Bar chart for average sales of each product
# plt.figure(figsize=(8, 6))
# plt.bar(products, average_sales, color=['blue', 'green', 'red', 'purple', 'orange'])
# plt.title('Average Sales for Each Product')
# plt.xlabel('Products')
# plt.ylabel('Average Sales')
# plt.show()
#
# # Pie chart for average sales of each product
# plt.figure(figsize=(8, 6))
# plt.pie(average_sales, labels=products, autopct='%1.1f%%', startangle=140)
# plt.title('Average Sales Distribution for Each Product')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
