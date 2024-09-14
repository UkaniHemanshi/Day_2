import sqlite3

try:
    conn = sqlite3.connect('School.db')

    cursor = conn.cursor()

    #to drop tables because same data was getting inserted multiple times
    cursor.execute('drop table students')
    cursor.execute('drop table courses')

# for exception handling checking
    # cursor.execute('''create table students(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,grade TEXT)''')

    cursor.execute('''create table if not exists students(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,grade TEXT)''')
    cursor.execute('''create table if not exists courses(course_id INTEGER PRIMARY KEY,course_name TEXT,instructor TEXT)''')

except sqlite3.Error as e:

    print("operation error:",e)

else:
    # table1
    cursor.execute("INSERT INTO students(id,name,age,grade)VALUES(1001,'Mayura','30','A')")
    cursor.execute("INSERT INTO students(id,name,age,grade)VALUES(1002,'Sachin','23','B')")
    cursor.execute("INSERT INTO students(id,name,age,grade)VALUES(1003,'Hemanshi','22','C')")
    cursor.execute("INSERT INTO students(id,name,age,grade)VALUES(1004,'Ankit','33','A')")
    cursor.execute("INSERT INTO students(id,name,age,grade)VALUES(1005,'Harsh','30','C')")

    # table 2
    cursor.execute("INSERT INTO courses(course_id,course_name,instructor)VALUES(001,'AI','Anjali Mam')")
    cursor.execute("INSERT INTO courses(course_id,course_name,instructor)VALUES(002,'Maths','Sajida Mam')")
    cursor.execute("INSERT INTO courses(course_id,course_name,instructor)VALUES(003,'Java','Nathan Sir')")

    # query database
    print(
        "----------------------------------------------Retrieve students with grade A-----------------------------------------------------------------------")
    print()

    cursor.execute('Select * from students where grade ="A"')
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

    print(
        "----------------------------------------------List courses by instructor name---------------------------------------------------------------------------------")
    print()

    cursor.execute('select * from courses order by course_name')
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        print(row)
    print()

    # update data
    cursor.execute("update students set grade = 'A' where name = 'Sachin'")
    results = cursor.fetchall()

    cursor.execute("update courses set instructor = 'Pratiksha Mam' where course_id = 001")
    results = cursor.fetchall()

    print(
        "---------------------------------------------updated students table--------------------------------------------------------------------------------------")
    print()

    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    print(results)

    print()

    print(
        "---------------------------------------------updated course table--------------------------------------------------------------------------------------")
    print()

    cursor.execute("SELECT * FROM courses")
    results = cursor.fetchall()
    print(results)

    print()

    # Delete
    cursor.execute('Delete from students where id=1005')
    print(
        "--------------------------------------------Deleted one record from student table----------------------------------------------------------------------")
    print()

    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    print(results)
    print()

    print(
        '=============================================================================================================================')
    print()
    # how to show tables
    cursor.execute("select name from sqlite_master where type='table'")
    results = cursor.fetchall()
    print(results)

finally:

    conn.commit()
    cursor.close()
    conn.close()