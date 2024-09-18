import sqlite3

conn = sqlite3.connect('hww.db')
cursor = conn.cursor()

cursor.execute('drop table subjects')
cursor.execute('drop table students')
cursor.execute('drop table students_details')

# Create the 'subjects' table
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
            subj_id INTEGER PRIMARY KEY,
            subj_name TEXT             
)''')

# Create the 'students' table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            stud_id INTEGER PRIMARY KEY,
            name TEXT
)''')


# Create the 'students_details' table with foreign keys
cursor.execute('''CREATE TABLE IF NOT EXISTS students_details 
            (
            stud_id INTEGER,
            subj_id INTEGER,
            marks INTEGER,
            FOREIGN KEY(stud_id) REFERENCES students(stud_id),                     
            FOREIGN KEY(subj_id) REFERENCES subjects (subj_id)                     
            )''')

# Insert some example data
cursor.execute("INSERT INTO subjects VALUES (1, 'AI')")
cursor.execute("INSERT INTO subjects VALUES (2, 'Maths')")
# Fetch and print data from 'subjects' table
cursor.execute('SELECT * FROM subjects')
sub = cursor.fetchall()
print("Subjects Table Data:")
for i in sub:
    print(i)

cursor.execute("INSERT INTO students VALUES (1, 'Hemanshi')")
cursor.execute("INSERT INTO students VALUES (2, 'Geet')")
# Fetch and print data from 'students' table
cursor.execute('SELECT * FROM students')
stu = cursor.fetchall()
print("\nStudents Table Data:")
for i in stu:
    print(i)

cursor.execute("INSERT INTO students_details VALUES (1, 1, 85)")
cursor.execute("INSERT INTO students_details VALUES (2, 2, 90)")

conn.commit()

# Fetch and print data from 'students_details' table
cursor.execute('SELECT * FROM students_details')
det = cursor.fetchall()
print("\nStudents Details Table Data:")
for i in det:
    print(i)

# Combine data from 'students', 'subjects', and 'students_details' tables
cursor.execute('''SELECT students.name, subjects.subj_name, students_details.marks 
            FROM students 
            JOIN students_details ON students.stud_id = students_details.stud_id
            JOIN subjects ON students_details.subj_id = subjects.subj_id''')

# Fetch and print combined result
res = cursor.fetchall()
print("\nCombined Data:")
for row in res:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
