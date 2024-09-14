import seaborn as sns
import matplotlib.pyplot as plt

#Load the Iris dataset
df = sns.load_dataset('iris')
print(df.head())

fig,axs = plt.subplots(2,2, figsize=(12,1))

#scatter plot petal length vs petal width
# axs[0,0].figure(figsize=(8,6))
scatter = axs[0,0].sns.scatterplot(x='petal_length', y='petal_width', hue='species',data=df,palette='Set2',s=100)
axs[0,0].title("scatter plot:petal length vs petal width.")
fig.colorbar(scatter,ax=axs[0,0])

#Box plot: sepal length by species
# axs[0,1].figure(figsize=(8,6))
box= axs[0,1].sns.boxplot(x='species', y='sepal_length', data=df,hue='species',palette='Set3')
axs[0,1].title("Box plot: sepal length by species")
fig.colorbar(box,ax=axs[0,1])
# plt.show()

#Violin plot: petal length by species.
# plt.figure(figsize=(8,6))
violin= axs[1,0].sns.violinplot(x='species', y='petal_length', data=df,palette='Pastel1')
axs[1,0].title("Violin plot: petal length by species.")
fig.colorbar(box,ax=axs[1,0])

#pair plot: Relationships between all features
pair=axs[1,1].sns.pairplot(df,hue='species',palette='Set1')
axs[1,1].title("pair plot: Relationships between all features")
fig.colorbar(box,ax=axs[1,1])