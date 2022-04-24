import sqlite3


def check_user(username):
    """
    Check if user exists in database
    :param username: username of the user
    :return: True if user exists, False if user does not exist
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False


def authenticate_user(username, password):
    """
    Authenticate user
    :param username: username of the user
    :param password: password of the user
    :return: True if user is authenticated, False if user is not authenticated
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False
