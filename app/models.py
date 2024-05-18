from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import validates
from datetime import datetime, timezone

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    points: so.Mapped[int] = so.mapped_column(sa.Integer)
    status: so.Mapped[str] = so.mapped_column(sa.String(7))
    committed = db.Column(db.Boolean, default=False)  # Add a committed field
    posts: so.Mapped[List['Post']] = so.relationship('Post', back_populates='author')

    @validates('username')
    def validate_username(self, key, username):
        if len(username) > 64:
            raise ValueError("Username cannot be longer than 64 characters")
        return username
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
    def __repr__(self):
        return f'<User {self.username}>'

    def is_committed(self):
        return self.committed  # Ensure this returns the committed field

    def mark_as_committed(self):
        self.committed = True
        db.session.add(self)
        db.session.commit()
    
class Post(db.Model):
    __tablename__ = "post"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(500))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.id'), index=True)

    author: so.Mapped[User] = so.relationship('User', back_populates='posts')

    def __repr__(self):
        return f'<Post {self.body}>'

class Thread(db.Model):
    __tablename__ = "thread"
    thread_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    post_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('post.id'))
    thread_name: so.Mapped[str] = so.mapped_column(sa.String(140))
    post: so.Mapped[Post] = so.relationship('Post', backref=so.backref('threads', lazy=True))

    def __repr__(self):
        return f'<Thread {self.thread_name}>'

class Response(db.Model):
    __tablename__ = "response"
    response_id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    post_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('post.id'), nullable=False)
    thread_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('thread.thread_id'), nullable=False)

    post: so.Mapped[Post] = so.relationship('Post', backref=so.backref('responses', lazy=True))
    thread: so.Mapped[Thread] = so.relationship('Thread', backref=so.backref('responses', lazy=True))
