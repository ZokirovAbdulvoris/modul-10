import sqlite3


db_connect = sqlite3.connect("python.sqlite3")

db_cursor = db_connect.cursor()


def create_table_users():
    db_cursor.execute("""
       CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY,
       first_name TEXT,
       last_name TEXT)
    """)


def create_table_product():
    db_cursor.execute("""
     CREATE TABLE IF NOT EXISTS product(
     id INTEGER PRIMARY KEY,
     title TEXT,
     price REAL)
     """)


def create_table_orders():
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    id INTAGER PRIMARY KEY,
    product_id INTEGER,
    user_id INTEGER)
""")


def insert_users(firstname, lastname):
    db_cursor.execute("""
   INSERT INTO users (first_name, last_name)
   VALUES(?, ?)""", (firstname, lastname))



# def alter_users():


    # db_cursor.execute("""
    # ALTER TABLE users ADD COLUMN age INTEGER DEFAULT  14
    # """)
    #

    # db_cursor.execute("""
    # ALTER TABLE users RENAME first_name to familiya
    #
    #
    # """)

    #
    # db_cursor.execute("""
    # UPDATE TABLE SET first_name='ism' WHERE first_name
    # """)


def insert_product(title, price):
    db_cursor.execute("""
    INSERT INTO product (title, price)
    VALUES(?, ?)""", (title, price))


def update_users():
    db_cursor.execute("""
    UPDATE users SET first_name='Jon',
    last_name='Doe' WHERE  id=1
    """)


def delete_users():
    db_cursor.execute("""
    DELETE FROM users WHERE id=1
    """)



def insert_orders(product_id, user_id):
    db_cursor.execute("""
    INSERT INTO orders (product_id, user_id)
    VALUES(?, ?)""", (product_id, user_id))




def read_users():
    db_cursor.execute("""
    SELECT * FROM users
    """)
    return db_cursor



db_connect.commit()

# alter_users()
print(read_users().fetchall())
db_connect.close()


