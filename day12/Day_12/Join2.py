import pandas as pd
import sqlite3



# 1 esatblish a connection to the database
conn = sqlite3.connect('student_database.db')
conn.execute('PRAGMA foreign_keys = 1')
cursor = conn.cursor()

# cursor.execute('drop table subjects')
# cursor.execute('drop table students')


# 2 create department table with primary key
cursor.execute(
    '''create table if not exists subjects(id INTEGER PRIMARY KEY,sub_name TEXT not null)''')

# 3 create employee table with primary key and foreign key
cursor.execute(
    '''create table if not exists students(stu_id INTEGER PRIMARY KEY,stu_name TEXT not null,sub_id INTEGER,marks INTEGER,foreign key (sub_id) references subjects(id))''')

# # 4 create indexes
# cursor.execute('''create index if not exists idx_subject_name on employees(emp_name)''')
# cursor.execute('''create index if not exists idx_department_name on departments(depart_name)''')

# 5 insert data into 'department'
cursor.execute("INSERT  INTO subjects(id,sub_name)VALUES(1,'Python')")
cursor.execute("INSERT  INTO subjects(id,sub_name)VALUES(2,'Maths')")
cursor.execute("INSERT INTO subjects(id,sub_name)VALUES(3,'AI')")


# 6 insert data inro emp
cursor.execute("INSERT  INTO students(stu_id,stu_name,sub_id,marks)VALUES(01,'mayura',1,89)")
cursor.execute("INSERT  INTO students(stu_id,stu_name,sub_id,marks)VALUES(02,'mayuresh',2,56)")
cursor.execute("INSERT  INTO students(stu_id,stu_name,sub_id,marks)VALUES(03,'sugandha',1,78)")
cursor.execute("INSERT INTO students(stu_id,stu_name,sub_id,marks)VALUES(04,'hemanshi',1,90)")

# Perform a JOIN query
query1 = '''
SELECT students.stu_id,students.stu_name,students.marks, subjects.sub_name
FROM students
JOIN subjects ON students.sub_id = subjects.id
'''
# Fetch and display results for query1= join
print("join\n")
cursor.execute(query1)
rows = cursor.fetchall()
for row in rows:
    print(f'stu_id: {row[0]}, stu_name: {row[1]},marks: {row[2]},sub_name: {row[3]}')

conn.commit()

conn.close()