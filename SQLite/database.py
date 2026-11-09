import sqlite3

# The code below will create a DataBase in memory which is temporary 
# connect = sqlite3.connect('Notes.db')

# Creates a DataBase which remains with our files
connect = sqlite3.connect('Notes.db')

# Create a cursor
c = connect.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
    )""")

# Data Types : NULL, INTEGER, REAL, TEXT, BLOB

# Commit our command
connect.commit()

# Close our connection
connect.close()