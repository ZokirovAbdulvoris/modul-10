import sqlite3

db_connect = sqlite3.connect("python.sqlite3")

db_cursor = db_connect.cursor()


db_cursor.execute("""
   CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY,  
   first_name TEXT,
   last_name TEXT)
""")

db_cursor.execute("""
     CREATE TABLE IF NOT EXISTS product(
     id INTEGER PRIMARY KEY,
     title TEXT,
     price REAL)
     """)

db_cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY,
id INTAGER PRIMARY KEY,
product_id INTEGER,
user_id INTEGER)
""")

db_cursor.execute("""
INSERT INTO users (first_name, last_name)
VALUES('Abdulvoris', 'Zokirov') 
""")


db_connect.commit()

db_connect.close()