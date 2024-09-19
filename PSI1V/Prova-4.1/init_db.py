import sqlite3

conn = sqlite3.connect('database.db')

SCHEMA = "database/SCHEMA.sql"

with open(SCHEMA) as f:
    conn.executescript(f.read())

# encerra operações
conn.commit()
conn.close()