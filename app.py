from flask import Flask, render_template, redirect, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db")




@app.route('/')
def home():  # put application's code here
    return render_template("home.html")

@app.route('/signup', methods=['POST','GET'])
def render_signup_page():   # put application's code here
    if request.method == 'POST':
        fname = request.form.get('user_fname').title().strip()
        lmame = request.form.get('user_lname').title().strip()
        email = request.form.get('user_email').lower().strip()
        password = request.form.get('user_password')
        password2 = request.form.get('user_password2')

        if password != password2:
            return  redirect("\signup?error=passwords+do+not+match")

        if int(password) < 8:
            return redirect("\signup?error=password+must+be+over+8+characters")

    return render_template("signup.html")
@app.route('/login', methods=['POST','GET'])
def render_login_page():  # put application's code here
    return render_template("login.html")


# sign up - input info into the database
# log in - checks if login data is in the database.
