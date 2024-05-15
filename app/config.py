import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
flaskApp = Flask(__name__)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI =  "sqlite:///" + os.path.join(basedir, 'test.db')
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI =  "sqlite:///:memory"
    TESTING = True
    



