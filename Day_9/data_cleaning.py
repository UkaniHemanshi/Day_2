import pandas as pd

data = {"Name":['Alice','Bob','Charlie'],"Age":[23,34,35],'City':['newyork','mathura','surat']}
df = pd.DataFrame(data)
print(df)

# adding new column score into existing dataframe

df['score'] = [87,56,78]
print(f"Dataframe after adding score column:\n{df}\n")

df['score'] = df['score'] +5
print(f"Dataframe after modifing score column:\n{df}\n")

sorted_by_age = df.sort_values(by='Age')
print(f"Dataframe sorted by age:\n{sorted_by_age}\n")

sorted_by_index = df.sort_index(ascending=False)
print(f"Dataframe sorted by index:\n{sorted_by_index}\n")

df = df.rename(columns={'score':'Final Score'})
print(f"Final dataframe after operation:\n{df}\n")

data_missing_value = {"Name":['Alice','Bob','Charlie'],"Age":[23,34,None],'City':['newyork',None,'surat']}
df = pd.DataFrame(data_missing_value)


print(f"Which column contains missing value:\n{df.isnull().sum()}\n")

df['Age'] = df["Age"].fillna(df["Age"].mean())
print(f"Dataframe after filling age:\n{df}\n")

df_drooped = df.dropna()
print(f"Dataframe after Dropping:\n{df_drooped}\n")

df['Name'] = df["Name"].replace({'Alice':"hemanshi",'Bob':'ankudi'})
print(f"after changing the name column:\n{df}\n")






