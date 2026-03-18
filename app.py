from flask import Flask, render_tenplate, request, redirect, session
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db"




@app.route('/')
def home():  # put application's code here
    return redirect("/")


# sign up - input info into the database
# log in - checks if login data is in the database.
