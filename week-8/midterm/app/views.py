from app import app
from flask import render_template

# app.route() instructs the program that when the user routes to a specific page they will be presented with what follows
# This is the default page that the server will direct you to upon connecting to localhost:5000
@app.route('/')
def hello():
    return "Hello World!"

# If you add a string after the address the page will route to this function like so: localhost:5000/Chris
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# Here we are rendering a full webpage containing HTML and CSS
@app.route('/index')
def index():
    return render_template("index.html")