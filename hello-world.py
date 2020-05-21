# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:14:08 2020

@author: Admin
"""
from flask import Flask

#instatiating the Flask Class. "__name__" references the name of the current module being worked with which is hello-world.py
app = Flask(__name__)

# Instaniating a routeRoute
@app.route('/users/<username>')

#Defining a function
def hello_world(username=None):    
    return("Hello {}!".format(username))
