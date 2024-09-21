import sqlite3

conn = sqlite3.connect("user_database.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,username TEXT, address TEXT,mobile INTEGER,email TEXT)''')

user_data = [
    ('john_doe', '123 Elm St, Springfield', '555-1234', 'john@example.com'),
    ('jane_smith', '456 Oak St, Springfield', '555-5678', 'jane@example.com'),
    ('bob_jones', '789 Pine St, Springfield', '555-8765', 'bob@example.com'),
    ('alice_brown', '101 Maple St, Springfield', '555-4321', 'alice@example.com'),
    ('charlie_black', '202 Birch St, Springfield', '555-1122', 'charlie@example.com'),
    ('david_white', '303 Cedar St, Springfield', '555-3344', 'david@example.com'),
    ('eve_green', '404 Willow St, Springfield', '555-5566', 'eve@example.com'),
    ('frank_yellow', '505 Spruce St, Springfield', '555-7788', 'frank@example.com'),
    ('grace_blue', '606 Ash St, Springfield', '555-9900', 'grace@example.com'),
    ('henry_red', '707 Chestnut St, Springfield', '555-2233', 'henry@example.com')
]

cursor.executemany('''INSERT INTO user (username, address, mobile, email)VALUES (?, ?, ?, ?)''', user_data)

print('All Recors:\n')
cursor.execute("SELECT * FROM user")
results=cursor.fetchall()
print(results)

name = input("Enter the username: ")
add = input("Enter the address: ")
mobile = int(input("Enter the phone_no: "))
email = input("Enter the email: ")

def check_user(username,address,mobile,email):
    cursor.execute("SELECT * FROM user WHERE username = ? AND address = ?", (username, address))
    result = cursor.fetchone()
    if result is not None:
        print(cursor.fetchall())
    else:
        cursor.execute('INSERT INTO user (username, address, mobile, email)VALUES (?, ?, ?, ?)', (username,address,mobile,email))
        conn.commit()
        print("User added")
check_user(name,add,mobile,email)

# Commit the changes
conn.commit()

cursor.close()

# Close the connection
conn.close()

