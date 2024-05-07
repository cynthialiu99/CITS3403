from typing import List, Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)

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
    