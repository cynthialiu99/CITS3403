from typing import List
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

class Users(db.Model):
    id = db.Column(db.string(8), primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    student_id = db.Column(db.String(8), primary_key=True)
    points = db.Column(db.Integer)
    def __repr__(self) -> str:
        return f'<Student {self.name} {self.uwa_id}>'
    
class Staff(db.Model):
    staff_id = db.Column(db.String(8), primary_key=True)
    points = db.Column(db.Integer)
    def __repr__(self) -> str:
        return f'<Student {self.name} {self.staff_id}>'
    
class Threads(db.Model):
    thread_id = db.Column(db.String(100), primary_key = True)
    creator_id = db.Column(db.String(8), nullable=False)
    content = db.Column(db.Text, nullable = False)

class responses(db.Model):
    thread_id = db.Column(db.String(100), nullable = False)
    response_id = db.Column(db.String(100), primary_key = True)
    response_no = db.Column(db.Integer, nullable = False)
    responder_id = db.Column(db.String(8), nullable = False)
    