import sqlite3
from data.login import check_user


def create_user(username, password, fname, lname, country, state, city, mobile, company):
    """
    Create a user in the database
    :param username: username of the user
    :param password: password of the user
    :param fname: first name of the user
    :param lname: last name of the user
    :param country: country of the user
    :param state: state of the user
    :param city: city of the user
    :param mobile: mobile of the user
    :return: True if user is created, False if user already exists
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    if not check_user(username):
        c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (username, password, fname, lname, country, state, city, mobile, company))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
