from random import sample
from django.shortcuts import render

from flask import Flask, jsonify, render_template, request
from flask_restful import Api

from data.add_to_cart import add_product_to_cart
from data.index import new_products, slider
from data.login import authenticate_user, check_user, user_logged_in
from data.register import create_user

app = Flask(__name__)
api = Api(app)

usernames = []


@app.route('/')
@app.route('/index.html')
def index_html():
    context = {
        'slider': slider,
        'new_products': new_products,
        # random sample
        'popular_products': sample(new_products, len(new_products)),
        'new_arrival': new_products,
        'best_seller': sample(new_products, len(new_products)),
        'special_offer': sample(new_products, len(new_products))
    }
    return render_template('index.html', context=context)


@app.route('/about.html')
def about_html():
    return render_template('about.html')


@app.route('/cart.html', methods=['GET', 'POST'])
@app.route('/cart/<int:product_id>', methods=['GET', 'POST'])
@app.route('/cart/<int:product_id>/<int:quantity>', methods=['GET', 'POST'])
def add_to_cart(product_id, quantity=1):
    """
    Add product to cart
    :return:
    """
    if request.method == 'POST':
        # check which user is logged in
        for user in usernames:
            if user_logged_in(user):
                add_product_to_cart(user, product_id, quantity)

                for product in new_products:
                    if product['id'] == product_id:
                        context = {
                            "cart": [
                                {
                                    "id": product['id'],
                                    "name": product['name'],
                                    "brand": product['brand'],
                                    "price": product['price'],
                                    "image": product['image'],
                                    "quantity": quantity
                                }
                            ]
                        }
                        return render_template('cart.html', context=context)

    return render_template('cart.html', error="No product found, check if you are logged in?")


@app.route('/checkout.html')
def checkout_html():
    return render_template('checkout.html')


@app.route('/contact.html')
def contact_html():
    return render_template('contact.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login_html():
    if request.method == 'POST':
        """
        Authenticate user
        """
        username = request.form.get('email')
        password = request.form.get('password')
        if check_user(username):
            if authenticate_user(username, password):
                usernames.append(username)
                return render_template('login_success.html')
            else:
                return render_template('404.html', error='Invalid username or password')
        else:
            return render_template('404.html', error='No user found with this username')
    else:
        return render_template('login.html')


@app.route('/my-account.html')
def my_account_html():
    return render_template('my-account.html')


@app.route('/order.html', methods=['GET', 'POST'])
def order_html():
    return render_template('order.html')


@app.route('/register.html', methods=['GET', 'POST'])
def register_html():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        country = request.form.get('country')
        mobile = request.form.get('mobile')
        state = request.form.get('state')
        city = request.form.get('city')
        company = request.form.get('company')
        is_logged_in = True

        if password == confirm_password:
            """`
            Create a user in the database if the username is not taken
            """
            if create_user(username, password, fname, lname, country, state, city, mobile, company, is_logged_in):
                # storing usernames to check login sessions laters on
                usernames.append(username)
                return render_template('register_success.html')
            else:
                return render_template('404.html', error='Username already exists')
        else:
            return render_template('404.html', error='Passwords do not match')
    else:
        return render_template('register.html')


@app.route('/shop.html')
def shop_html():
    context = {
        'products': new_products
    }
    return render_template('shop.html', context=context)


@app.route('/single-product.html/<int:id>')
def single_product(id):
    for product in new_products:
        if product.get("id") == id:
            context = {
                "product": product
            }
            return render_template('single-product.html', context=context)

    for product in slider:
        if product.get("id") == id:
            context = {
                "product": product
            }
            return render_template('single-product.html', context=context)


@app.route('/wishlist.html')
def wishlist_html():
    return render_template('wishlist.html')
