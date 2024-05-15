from wtforms import SelectField, PasswordField, StringField, SubmitField, HiddenField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import *

class CreateThreadForm(FlaskForm):
    title = StringField("Enter title:", validators=[DataRequired()])
    content = StringField("Enter thread content:", validators=[DataRequired()])
    submit = SubmitField("Create thread")

    def create_thread(self, user_id):

        if (is_table_empty(Post) == True):
            postid = 0
        else:
            postid = db.session.query(sa.func.max(Post.id)).scalar() or 0
            postid += 1

        if (is_table_empty(Thread) == True):
            threadid = 0
        else:
            threadid = db.session.query(sa.func.max(Thread.id)).scalar() or 0
            threadid += 1
        # Create a new post
        post = Post(id = postid, body = self.content.data, user_id = user_id)
        thread = Thread(thread_id = threadid, post_id = postid, thread_name = self.title.data)

        # Add the post to the database session
        db.session.add(post)
        db.session.add(thread)
        db.session.commit()

        return post.id, thread.thread_id


class ReplyThreadForm(FlaskForm):
    def reply_thread(self, user_id):
        postid = CreateThreadForm.create_thread()[0]
        threadid = CreateThreadForm.create_thread()[1]
        post = Post(id = postid, body = self.content.data, user_id = user_id)
        thread = Thread(thread_id = threadid, post_id = postid)
        content = StringField("Enter reply:", validators=[DataRequired()])
        reply = Response(p_id = postid, t_id = threadid, body=content, user_id = user_id)

        db.session.add(reply)
        db.session.commit()


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")
    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is None:
            raise ValidationError('Account does not exist')


class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email2 = StringField('Confirm Email', validators=[DataRequired(), EqualTo('email')])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    type = HiddenField()
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
    def create_user(self):
        if (is_table_empty(User) == True):
            userid = 0
        else:
            userid = db.session.query(sa.func.max(User.id)).scalar() or 0
            userid += 1
        user = User(id = userid, username = self.username.data, email = self.email.data, points = 0, status = self.type.data)
        user.set_password(self.password.data)

        db.session.add(user)
        db.session.commit()

        print(db.session.scalar(sa.select(User)))

def is_table_empty(tablename):
    # Execute a query to count the number of records in the Threads table
    count = tablename.query.count()

    # Check if the count is zero
    if count == 0:
        return True
    else:
        return False