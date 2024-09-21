import pandas as pd
import numpy as np

emp_name = ["Sachin","Hemanshi","Dhruv","Harshal","Geetika"]
emp_id = [1001,1002,1003,1004,1005]
comp_name = ["TCS","Wipro","Google","Amazon","CDAC"]

df1 = pd.DataFrame({'emp_name':emp_name,'emp_id':emp_id,'comp_name':comp_name})

salary = [2000,1000,5000,8000,7000]
df2 = pd.DataFrame({'emp_id':emp_id,'salary':salary})

df3 = df1.merge(df2,on='emp_id')

print(df3)
