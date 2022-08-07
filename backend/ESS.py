""" 
I am placing all the needd and use libraries and modules here to reduce mport redanduncy

"""

# the server and api app
import os
from datetime import datetime
import urllib.request, json

import httpx
from flask import Flask, redirect, request, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, url_for, redirect, Response
from flask import flash

from Database.database import  Library

# declaring the flask initilizer
app = Flask(__name__)
# using sqlalchemy for the db managment and using sqlite as my goto db 
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Library.db'
# initlizing the db
db = SQLAlchemy(app)