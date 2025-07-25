
import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('sample_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
''', [
    ('Alice', 'HR', 50000),
    ('Bob', 'IT', 60000),
    ('Charlie', 'Finance', 55000)
])

# Commit changes
conn.commit()

# Select and display all data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("Employee Records:")
for row in rows:
    print(row)

# Close connection
conn.close()
