import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

employees = [
    ("Rahul", "HR", 50000),
    ("Reshma", "AI", 80000),
    ("Kiran", "Sales", 45000),
    ("Anu", "IT", 70000),
    ("David", "AI", 90000)
]

cursor.executemany(
    "INSERT INTO employees(name, department, salary) VALUES(?,?,?)",
    employees
)

conn.commit()

print("Database Created")