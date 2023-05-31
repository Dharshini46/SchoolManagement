from create import UserProfile
import jsonify
from flask import request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:dharshini#06@localhost/new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/api/students/', methods=['POST'])
def retrieve_student():
   student = db.session.query(UserProfile)
@app.route('/api/student/add/', methods=['POST'])
def user():
    roll_number = request.form['roll_number']
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    mark = request.form['mark']
    student = UserProfile(roll_number=roll_number,name=name,date_of_birth=date_of_birth,mark=mark)
    db.session.add()
    db.session.commit()
@app.route('/api/student/<pk>/', methods=['GET'])
def retrieve_student(pk):
   
   stud = db.session.query(UserProfile).filter_by(roll_number = pk)
   return jsonify ({'results':pk})
@app.route('/api/student/add/', methods=['POST','GET'])
def func(pk):
  mark = request.form[mark]
@app.route('/api/student/add/', methods=['GET'])
def func(pk):
    mark = db.session.query(UserProfile.mark).filter_by(roll_number = pk)
    return jsonify




