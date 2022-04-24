from flask import Flask, jsonify, render_template, request
from flask_restful import Api

from data.index import banner, slider
from data.login import authenticate_user, check_user
from data.register import create_user

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
        'slider': slider,
        'banner': banner
    }
    return render_template('index.html', context=context)


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


@app.route('/order.html')
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

        if password == confirm_password:
            """`
            Create a user in the database if the username is not taken
            """
            if create_user(username, password, fname, lname, country, state, city, mobile, company):
                return render_template('register_success.html')
            else:
                return render_template('404.html', error='Username already exists')
        else:
            return render_template('404.html', error='Passwords do not match')
    else:
        return render_template('register.html')


@app.route('/shop.html')
def shop_html():
    return render_template('shop.html')


@app.route('/single-product.html/<int:id>')
def single_product(id):
    for product in banner:
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
