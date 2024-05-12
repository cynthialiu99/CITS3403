from typing import List, Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timezone

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64))
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    points: so.Mapped[int] = so.mapped_column (sa.Integer)
    status: so.Mapped[str] = so.mapped_column(sa.String(7))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Threads(db.Model):
    thread_id: so.Mapped[str] = so.mapped_column(sa.String(100), primary_key=True)
    post_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey(Post.id))

class Responses(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('responses', lazy=True))

    thread_id = db.Column(db.String(100), db.ForeignKey('threads.thread_id'), nullable=False)
    thread = db.relationship('Threads', backref=db.backref('responses', lazy=True))

    response_id = db.Column(db.String(100), primary_key=True)
    response_no = db.Column(db.Integer, nullable=False)
    responder_id = db.Column(db.String(8), nullable=False)

# class Responses(db.Model):
#     post_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Post.id), sa.Integer)
#     thread_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Threads.id), sa.String(100), nullable=False)
#     response_id: so.Mapped[str] = so.mapped_column(sa.String(100), primary_key=True)
#     response_no: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
#     responder_id: so.Mapped[str] = so.mapped_column(sa.String(8), nullable=False)
