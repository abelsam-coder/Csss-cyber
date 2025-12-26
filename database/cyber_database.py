import sqlite3
database = sqlite3.connect('cyber.db')
cursor = database.cursor()
cursor.execute("CREATE TABLE users (email TEXT,username TEXT,password TEXT)")
database.commit()