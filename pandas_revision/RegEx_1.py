import re
import pandas as pd

with open("records.csv",'r') as file:
    data = file.readlines()

pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})'
date_time_list = []
for line in data:
    match = re.search(pattern, line)
    if match:
        date_time_list.append(match.group(0))

print(date_time_list)
Date = []
Time = []
for i in date_time_list:
    date,time = i.split("T")
    Date.append(date)
    Time.append(time)

print(f"\nDate: {Date}")
print(f"\nTime: {Time}")

df = pd.read_csv("records.csv")
df = df.drop(columns="datetime")
df["Date"] = Date
df["Time"] = Time
df.to_csv("records_new.csv",index=False)
print(f"Result dataframe: {df}")