from flask import Flask, jsonify, render_template, request
from flask_restful import Api

from data.index import slider

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about_html():
    return render_template('about.html')


@app.route('/cart.html')
def cart_html():
    return render_template('cart.html')


@app.route('/checkout.html')
def checkout_html():
    return render_template('checkout.html')


@app.route('/contact.html')
def contact_html():
    return render_template('contact.html')


@app.route('/index.html')
def index_html():
    context = {
        'slider': slider
    }
    return render_template('index.html', context=context)


@app.route('/login.html')
def login_html():
    return render_template('login.html')


@app.route('/my-account.html')
def my_account_html():
    return render_template('my-account.html')


@app.route('/order.html')
def order_html():
    return render_template('order.html')


@app.route('/shop.html')
def shop_html():
    return render_template('shop.html')


@app.route('/single-product.html')
def single_product():
    return render_template('single-product.html')


@app.route('/wishlist.html')
def wishlist_html():
    return render_template('wishlist.html')
