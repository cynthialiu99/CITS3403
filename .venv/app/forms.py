from wtforms import SelectField, PasswordField, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

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

class StudentSignUp(FlaskForm):
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


