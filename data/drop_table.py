import sqlite3


def drop_table(table_name):
    """
    Drop a table in the database
    :param table_name: name of the table you want to drop
    :return: None
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS " + table_name)
    conn.commit()
    conn.close()


drop_table('users')
