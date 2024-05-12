import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
flaskApp = Flask(__name__)

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'potatoes-are-the-best'