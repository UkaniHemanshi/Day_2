import pandas as pd
import sqlite3

#1 esatblish a connection to the database
conn = sqlite3.connect('company.db')
conn.execute('PRAGMA foreign_keys = 1')
cursor = conn.cursor()

cursor.execute('drop table employees')
cursor.execute('drop table departments')

#2 create department table with primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT
)
''')

#3 create employee table with primary key and foreign key
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
''')
# 5 insert data into 'department'
cursor.execute('INSERT INTO departments (id, department_name) VALUES (1, "HR")')
cursor.execute('INSERT INTO departments (id, department_name) VALUES (2, "Engineering")')
cursor.execute('INSERT INTO departments (id, department_name) VALUES (3, "AI")')

# 6 insert data inro emp
cursor.execute('INSERT INTO employees (id, name, department_id) VALUES (1, "Alice", 1)')
cursor.execute('INSERT INTO employees (id, name, department_id) VALUES (2, "Bob", 2)')
cursor.execute('INSERT INTO employees (id, name, department_id) VALUES (3, "Charlie", 1)')

# Perform a JOIN query
query1 = '''
SELECT employees.name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.id
'''

# Simulate a RIGHT JOIN query
query2 = '''
SELECT employees.name, departments.department_name
FROM departments
LEFT JOIN employees ON departments.id = employees.department_id

UNION

SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
'''



# Fetch and display results for query1= join
print("join\n")
cursor.execute(query1)
rows = cursor.fetchall()
for row in rows:
    print(f'Employee: {row[0]}, Department: {row[1]}')



# Fetch and display results for query2=right join
print("\nright_join\n")
cursor.execute(query2)
rows = cursor.fetchall()
for row in rows:
    print(f'Employee: {row[0]}, Department: {row[1]}')

# Commit changes and close the connection
conn.commit()
conn.close()






