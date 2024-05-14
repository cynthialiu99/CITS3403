from wtforms import SelectField, PasswordField, StringField, SubmitField, EmailField
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
            postid = postid + 1

        if (is_table_empty(Threads) == True):
            threadid = 0
        else:
            threadid = threadid + 1
        # Create a new post
        post = Post(id = postid, body = self.content.data, user_id = user_id)
        thread = Threads(thread_id = threadid, post_id = postid)

        # Add the post to the database session
        db.session.add(post)
        db.session.add(thread)
        db.session.commit()

    #class ReplyThreadForm(FlaskForm):
    #content = StringField("Enter reply:", validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
    #redirect to forgot_password page if user clicks on forgot password??
    #redirect to Account page (Account.html)??

class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
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
            userid = userid + 1
        user = User(id = userid, username = self.username.data, email = self.email.data, points = 0)
        user.set_password(self.password.data)

        db.session.add(user)
        db.session.commit()

    #name
    #id
    #email
    #password
    #submit
    #redirect to login page

#class StaffSignUp(FlaskForm):
    #name
    #id
    #email
    #password
    #submit
    #redirect to login page


def is_table_empty(tablename):
    # Execute a query to count the number of records in the Threads table
    count = tablename.query.count()

    # Check if the count is zero
    if count == 0:
        return True
    else:
        return False