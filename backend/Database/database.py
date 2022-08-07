from ESS import *
from ESS import db

# creating the needed tables in out db
class Library(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   author = db.Column(db.String(100))
   book_name = db.Column(db.String(50))  
   comments = db.Column(db.Text())


# adding data
