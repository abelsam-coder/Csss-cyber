import sqlite3
database = sqlite3.connect('cyber.db')
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT,username TEXT,password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS security (username TEXT,ctf_point INTEGER,courses_completed INTEGER,level TEXT,ctf_completed INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS ctf_challenges (title TEXT, description TEXT, points INTEGER,img TEXT)")
database.commit()