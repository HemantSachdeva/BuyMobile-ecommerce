import sqlite3


def add_product_to_cart(username, product_id, quantity):
    """
    Add a product to cart (table in our db)
    :param username: username of the user
    :param product_id: id of the product
    :param quantity: quantity of the product
    """
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    # check if product is already in cart
    c.execute("SELECT * FROM cart WHERE username=? AND product_id=?",
              (username, product_id))
    product = c.fetchone()
    if product:
        # product is already in cart
        # update quantity
        c.execute("UPDATE cart SET quantity=? WHERE username=? AND product_id=?",
                  (quantity, username, product_id))
    else:
        # product is not in cart
        # add product to cart
        c.execute("INSERT INTO cart (username, product_id, quantity) VALUES (?, ?, ?)",
                  (username, product_id, quantity))
    conn.commit()
    conn.close()
