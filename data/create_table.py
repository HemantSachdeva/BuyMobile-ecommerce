import sqlite3


def create_user_table():
    """
    Create a table in the database
    :param table_name: name of the table
    :return: None
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password REAL, fname TEXT, lname TEXT, country TEXT, state TEXT, city TEXT, mobile TEXT, company TEXT, is_logged_in BOOLEAN)")
    conn.commit()
    conn.close()


create_user_table()


def create_cart_table():
    """
    Create a table in the database
    :return: None
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, product_id INTEGER, quantity INTEGER)")
    conn.commit()
    conn.close()


create_cart_table()
