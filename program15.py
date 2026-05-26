import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Rahul", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Anjali", 22))
conn.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Student Records:")
for row in rows:
    print(row)
conn.close()
"""Student Records:
(1, 'Rahul', 21)
(2, 'Anjali', 22)"""