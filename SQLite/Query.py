import sqlite3

connect = sqlite3.connect('Notes.db')

c = connect.cursor()

# Query the DataBase
c.execute("SELECT rowid, * FROM customers")

### c.fetchmany(3) 
### c.fetchone() --> returns data of first record in tuple datatype

items = c.fetchall()
for item in items:
    print(item)

connect.commit()
connect.close()