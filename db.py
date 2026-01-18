import sqlite3

conn = sqlite3.connect("students.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS admin(
          U_Name TEXT,
          Pass TEXT
          )
""")
conn.commit()
c.execute(
    "INSERT INTO admin (U_Name, Pass) VALUES (?, ?)",
    ("admin", "admin")
    )
conn.commit()
c.execute(
    "INSERT INTO admin (U_Name, Pass) VALUES (?, ?)",
    ("admin1", "password")
    )
conn.commit()
c.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    roll TEXT UNIQUE,
    department TEXT,
    year INTEGER
)
""")
conn.commit()

c.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    student_roll TEXT,
    date TEXT,
    status TEXT
)
""")
conn.commit()
conn.close()

def admin_login(U_Name, Pass):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    # This query checks if the username and password exist in the admin table
    c.execute("SELECT * FROM admin WHERE U_Name=? AND Pass=?", (U_Name, Pass))
    data = c.fetchone()
    conn.close()
    return data # Returns the user row if found, else Nonev

def add(name, roll, dept, year):
    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute(
            "INSERT INTO students(name, roll, department, year) VALUES (?,?,?,?)",
            (name, roll, dept, year)
        )
    conn.commit()
    conn.close()
    
def view(s,):
    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute(
        "SELECT * FROM students WHERE roll=?",(s,)
    )
    data = c.fetchall()
    return data
conn.close()
    

def view_a():
    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute(
        "SELECT * FROM students"
    )
    data=c.fetchall()
    return data
conn.close()
    

def delete(s):
    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute(
    "DELETE FROM students WHERE roll = ?",
    (s,))
    conn.commit()
conn.close()

def add_attendance(student,status,att_date):
    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute(
        "INSERT INTO attendance(student_roll,date,status) VALUES (?,?,?)",
        (student[0], str(att_date), status)
    )
    conn.commit()
conn.close()

def record():
    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute("""
    SELECT * FROM attendance
    """)
    data=c.fetchall()
    return data
conn.close()

def admin(U_Name,Pass):

    conn=sqlite3.connect("students.db")
    c=conn.cursor()
    c.execute("""
    SELECT * FROM
""")



