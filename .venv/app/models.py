from typing import List
from app import db

class Student(db.Model):
    uwa_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    def __repr__(self) -> str:
        return f'<Student {self.name} {self.uwa_id}>'
    
class Staff(db.model):
    staff_id = db.column(db.String(8), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable=False)
    def __repr__(self) -> str:
        return f'<Student {self.name} {self.staff_id}>'
    