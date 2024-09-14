import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
y1 = np.array([1,3,4,7,9,12,15,18,19,22])
y2 = np.array([2,5,7,10,12,13,16,18,21,23])

#subplots
fig,axs = plt.subplots(2,2, figsize=(12,10))

#line plot
# plt.figure(figsize=(8,6))
axs[0,0].plot(x,y1,label='Dataset1',color='Blue',marker='o',linestyle='--')
axs[0,0].plot(x,y2,label='Dataset2',color='red',marker='s',linestyle='-')
axs[0,0].set_title('line plot example')
axs[0,0].set_xlabel('X axis')
axs[0,0].set_ylabel('Y axis')
axs[0,0].legend()
axs[0,0].grid(True)

#barchart
categories = ['categoryA','categoryB','categoryC','categoryD']
values = [4,7,1,8]

# plt.figure(figsize=(8,6))
axs[0,1].bar(categories,values,color='purple')
axs[0,1].set_title('Bar Chart example')
axs[0,1].set_xlabel('categories')
axs[0,1].set_ylabel('values')


##scatter plot

x= np.random.rand(50)
y= np.random.rand(50)
colors = np.random.rand(50)
size = 1000*np.random.rand(50)

# plt.figure(figsize=(8,6))
scatter=axs[1,0].scatter(x,y,c=colors,s=size,alpha=0.5,cmap='viridis')
axs[1,0].set_title('Scatter plot example')
axs[1,0].set_xlabel('X axis')
axs[1,0].set_ylabel('Y axis')
fig.colorbar(scatter,ax=axs[1,0])

#piechart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales_data = np.random.randint(50, 500, size=(12, 5))

# Calculate average sales for each product
average_sales = np.mean(sales_data, axis=0)

# plt.figure(figsize=(8, 6))
axs[1,1].pie(average_sales, labels=products, autopct='%1.1f%%', startangle=140)
axs[1,1].set_title('Average Sales Distribution for Each Product')
axs[1,1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()

plt.show()
