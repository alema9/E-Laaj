from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doctor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  surname = db.Column(db.Text, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  speciality = db.Column(db.Text, nullable=False)
  phone = db.Column(db.Integer, nullable=False)
  licenseId = db.Column(db.Integer, nullable=False)
  yoe = db.Column(db.Integer, nullable=False)
  location = db.Column(db.Text, nullable=False)

class Patient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  surname = db.Column(db.Text, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  phone = db.Column(db.Integer, nullable=False)
  

def init_db():
  db.drop_all()
  db.create_all()