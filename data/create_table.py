import sqlite3


def create_table(table_name):
    """
    Create a table in the database
    :param table_name: name of the table
    :return: None
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password REAL, fname TEXT, lname TEXT, country TEXT, state TEXT, city TEXT, mobile TEXT, company TEXT)".format(table_name))
    conn.commit()
    conn.close()


create_table('users')
