import pandas as pd

emp_id = [1,2,3,4,5]
emp_name = ['hemanshi','sachin','dhruv','harshal','mina']

comapny_name = ['TCS','Google','Amazon','Meta','PWC']
salary = [100000,20000,30000,40000,500000]

df1 = pd.DataFrame({'Emp_id':emp_id,'Emp_name':emp_name})
df2 = pd.DataFrame({"Emp_id":emp_id,"Comany_name":comapny_name,"Salary":salary})

df3 = pd.merge(df1,df2,on="Emp_id")
print(df3)
