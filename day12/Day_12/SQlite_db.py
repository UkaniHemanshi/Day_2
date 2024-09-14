import sqlite3

#1.Establish connection
conn = sqlite3.connect('DAIBatch2024.db')

#2.Create a cursor object
cursor = conn.cursor()
cursor.execute('drop table users')
#3.create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')

#4.Insert some data
cursor.execute("INSERT INTO users(name,age)VALUES('Mayura','30')")
cursor.execute("INSERT INTO users(name,age)VALUES('Sachin','23')")
cursor.execute("INSERT INTO users(name,age)VALUES('Hemanshi','22')")
cursor.execute("INSERT INTO users(name,age)VALUES('Ankit','33')")

# #5.Commit the transcation to save the changes
conn.commit()
print('All Recors:\n')
cursor.execute("SELECT * FROM users")
results=cursor.fetchall()
print(results)
print('Order by clause:\n')
cursor.execute("select * from users order by age")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)
#7.Query with group by
print('\nusers groupe age with count:')
cursor.execute('select age, COUNT(*) as count from users GROUP by age')
results = cursor.fetchall()
for row in results:
    print(row)

cursor.execute("update users set age = 22 where name = 'Ankit'")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.execute("select* from users where name like 'Ankit'")
results = cursor.fetchall()
print(results)
cursor.close()

conn.close()