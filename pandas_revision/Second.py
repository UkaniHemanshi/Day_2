import pandas as pd
import numpy as np

student_df = pd.read_csv("students.csv")
extra_scores_df = pd.read_csv("Extra_scores.csv")

#clean data
print('=====================================Checking null values===========================================================================================================================')

print(student_df.isnull().sum())

print('=====================================Removing the rows where age column has nissing values==========================================================================================')
print()

student_df = student_df.dropna(subset="Age")
print(student_df)
print()

print('=====================================Filling missing values=========================================================================================================================')
print()


mean_value = student_df["Score"].mean()
student_df["Score"] = student_df["Score"].fillna(mean_value)
print(student_df)
print()

#prepare data
print('=====================================filter data: Score more than 70 and age greater than 20========================================================================================')
print()


student_df = student_df[(student_df['Score']>70) & (student_df['Age']>20)]
print(student_df)
print()

print('======================================Final Score================================================================================================================================')
print()

student_df['Final_score'] =student_df['Score']+10
print(student_df)
print()

print('========================================Removing Gender column=====================================================================================================================')
print()

student_df = student_df.drop(columns='Gender')
print(student_df)
print()

print('=========================================Sorting by final_score in descending order=================================================================================================')
print()

student_df = student_df.sort_values(by='Final_score',ascending=False)
print(student_df)
print()

print('==========================================Merging dataframes=======================================================================================================================')
print()

df3 = student_df.merge(extra_scores_df,on='ID')
print(df3)
print()

print('===========================================calculating total score================================================================================================================')
print()

df3['Total_score'] = df3['Final_score']+df3['Additional_Score']
print(df3)
print()

print('=============================================filling missing values in addtional_socre with zero===================================================================================')


df3['Additional_Score'] = df3['Additional_Score'].fillna(0)
print(df3)

