from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Testmanagement@localhost/new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class UserProfile(db.Model):
     roll_number = db.Column(db.String(50),primary_key = True)
     name = db.Column(db.String(255))
     date_of_birth = db.Column(db.Date)
     mark = db.Column(db.Integer)
     
if __name__ == '__main__':
    db.create_all()




