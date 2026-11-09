import sqlite3

# The code below will create a DataBase in memory which is temporary 
# connect = sqlite3.connect('Notes.db')

# Creates a DataBase which remains with our files
connect = sqlite3.connect('Notes.db')

# Create a cursor
c = connect.cursor()

# Inserting Records
many_records = [('Renu', 'Gupta', 'Renurg.it@gmail.com'), ('Navneet', 'Gupta', 'Navneetgta@gmail.com'), ('Atharv', 'Gupta', 'Atharvgupta@gmail.com')]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_records)

# Data Types : NULL, INTEGER, REAL, TEXT, BLOB

# Commit our command
connect.commit()

# Close our connection
connect.close()