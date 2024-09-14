import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
y1 = np.array([1,3,4,7,9,12,15,18,19,22])
y2 = np.array([2,5,7,10,12,13,16,18,21,23])

#line plot
plt.figure(figsize=(8,6))
plt.plot(x,y1,label='Dataset1',color='Blue',marker='o',linestyle='--')
plt.plot(x,y2,label='Dataset2',color='red',marker='s',linestyle='-')
plt.title('line plot example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True)
plt.show()

#barchart
categories = ['categoryA','categoryB','categoryC','categoryD']
values = [4,7,1,8]

plt.figure(figsize=(8,6))
plt.bar(categories,values,color='purple')
plt.title('Bar Chart example')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()


##scatter plot

x= np.random.rand(50)
y= np.random.rand(50)
colors = np.random.rand(50)
size = 1000*np.random.rand(50)

plt.figure(figsize=(8,6))
plt.scatter(x,y,c=colors,s=size,alpha=0.5,cmap='viridis')
plt.title('Scatter plot example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.colorbar()
plt.show()
