import sqlite3 as lite

con = lite.connect('FridayProj5.db')

with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print(f"SQLite version: {data[0]}")

    print("Table records:")
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    print(cursor.fetchall())