import pandas as pd
import seaborn as sns
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

day = np.arange(1,21)
temp = np.random.uniform(15,31,size=20)
humidity = np.random.randint(40,91,size=20)
df=pd.DataFrame({'day':day,'temp':temp,'humidity':humidity})

df.to_csv('temp-seaborn-data.csv')

with open('temp-seaborn-data.csv', 'r') as file:
    lines = file.readlines()
    print(lines)


#scatter plot petal length vs petal width
plt.figure(figsize=(8,6))
sns.scatterplot(x='humidity', y='temp',data=df)
plt.title("scatter plot")
plt.show()


# line chart
plt.figure(figsize=(8,6))
sns.lineplot(x='temp', y='day',data=df)
plt.title("line plot")
plt.show()

#box plot
plt.figure(figsize=(8,6))
sns.boxplot(y='temp', data=df)
plt.title("Box plot: ")
plt.show()

#hist plot
plt.hist(x='humidity',data=df)
plt.title('Histogram ')
plt.xlabel('Humidity')
plt.ylabel('Frequency')
plt.show()
