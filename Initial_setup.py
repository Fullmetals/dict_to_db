import sqlite3

# Connect to the database
connection = sqlite3.connect('vocabulary.db')

# Create the cursor, allowing you to traverse the records
cursor = connection.cursor()

# Create table
cursor.execute('''
CREATE TABLE vocabulary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    part_of_speech TEXT NOT NULL,
    definition TEXT NOT NULL
)
''')

# Commit the changes and close the connection
connection.commit()
connection.close()