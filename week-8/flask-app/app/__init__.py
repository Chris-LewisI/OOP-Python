# In order to use the Flask module you must first import it into the program
from flask import Flask

# Here we are naming the server client "app" so that we can call it as we go along the porgram
app = Flask(__name__)

# Here we import the views.py so that we can control our routing and directories
from app import views