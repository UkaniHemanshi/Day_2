import seaborn as sns
import matplotlib.pyplot as plt

#Load the Iris dataset
df = sns.load_dataset('iris')
print(df.head())

#scatter plot petal length vs petal width
plt.figure(figsize=(8,6))
sns.scatterplot(x='petal_length', y='petal_width', hue='species',data=df,palette='Set2',s=100)
plt.title("scatter plot:petal length vs petal width.")
plt.show()

#Box plot: sepal length by species
plt.figure(figsize=(8,6))
sns.boxplot(x='species', y='sepal_length', data=df,hue='species',palette='Set3')
plt.title("Box plot: sepal length by species")
plt.show()

#Violin plot: petal length by species.
plt.figure(figsize=(8,6))
sns.violinplot(x='species', y='petal_length', data=df,palette='Pastel1')
plt.title("Violin plot: petal length by species.")
plt.show()

#pair plot: Relationships between all features
sns.pairplot(df,hue='species',palette='Set1')
plt.title("pair plot: Relationships between all features")
plt.show()