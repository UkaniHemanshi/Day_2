import pandas as pd

df = pd.read_csv("country_vaccinations.csv")
print(f"First 5 rows of data:\n{df.head(5)}\n")
# changing name of column name
df = df.rename(columns={'iso_code':'country_code'})

# rename index to start from 1 insted of 0
df.index = range(1, len(df) + 1)

# handling missing data
df['people_fully_vaccinated'] = df["people_fully_vaccinated"].fillna(0)
print(df.isnull().sum())

df["vaccination_rate(%)"] = (df["people_vaccinated"]/200000)*100
print(f"After adding vaccination_rate:\n{df.head(3)}\n")


df['daily_vaccinations'] = df["daily_vaccinations"].fillna(df["daily_vaccinations"].mean())
print(f"After filling daily_vaccinations with mean value of column:\n{df}\n")

# df.drop('source_name', axis=1, inplace=True)
sorted_by_total_vaccinations = df.sort_values(by="total_vaccinations",ascending=False)
print(sorted_by_total_vaccinations.iloc[1:4,1:5])

print(df)
print(df.iloc[1:4,4:6])
df.to_csv("country_vaccinations.csv",index=False)
sorted_by_total_vaccinations.to_csv("country_vaccinations.csv",index=False)
