from flask import Flask, render_template, redirect
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db")




@app.route('/')
def home():  # put application's code here
    return render_template("home.html")

@app.route('/signup', methods=['POST','GET'])
def render_signup_page():  # put application's code here
    return render_template("signup.html")

@app.route('/login', methods=['POST','GET'])
def render_login_page():  # put application's code here
    return render_template("login.html")


# sign up - input info into the database
# log in - checks if login data is in the database.
