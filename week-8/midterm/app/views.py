from app import app
from flask import render_template, request, redirect, url_for

# app.route() instructs the program that when the user routes to a specific page they will be presented with what follows
# This is the default page that the server will direct you to upon connecting to localhost:5000
@app.route('/')
def hello():
    return "<center><h1>Hello World!</center></h1>"

@app.route('/login', methods=["GET", "POST"])
def login():
    # checks to see what the property of the method is to know how to go about the next step
    if request.method == "POST":
        user = request.form['nm']
        if (user):
            return redirect(url_for('success',name = user))
        else:
            return '<center><h1>Input for name is required</h1></center>'
    else:
        return "<center><h1>POST request is required</h1></center>"

# If you add a string after the address the page will route to this function like so: localhost:5000/success/Chris
@app.route('/success/<name>')
def success(name):
    if (name == ''):
        return '<center><h1>Please enter a name<h1></center>'
    else:
        return '<center><h1>Welcome %s<h1></center>' % name

# Here we are rendering a full webpage containing HTML and CSS
@app.route('/index')
def index():
    return render_template("index.html")