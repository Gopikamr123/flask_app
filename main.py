
import sqlite3
import os


if os.path.exists("abc.db"):
    os.remove("abc.db")


db_file = "abc.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)""")


def add_details(conn, name, age, grade):
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)", (name, age, grade))
    conn.commit()
    print(f"Added {name} successfully.")

def delete_student(conn, student_id):
    """Deletes a student based on their unique ID."""
    cur = conn.cursor()
    
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student with ID {student_id} deleted (if they existed).")


add_details(conn, "Alice", 20, "A")
add_details(conn, "Bob", 22, "B")
add_details(conn, "Charlie", 21, "C")


print("\nTable data before deletion:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)


delete_student(conn, 2)


print("\nTable data after deletion:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

conn.close()