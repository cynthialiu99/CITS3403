from wtforms import SelectField, PasswordField, StringField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

class CreateThreadForm(FlaskForm):
    title = StringField("Enter title:", validators=[DataRequired()])
    content = StringField("Enter thread content:", validators=[DataRequired()])
    submit = SubmitField("Create thread")

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


