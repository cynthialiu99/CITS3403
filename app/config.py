import os
from flask import Flask
from app.__init__ import Config
from flask_sqlalchemy import SQLAlchemy
from app.models import User

# Initialize the Flask application
basedir = os.path.abspath(os.path.dirname(__file__))
flaskApp = Flask(__name__)

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True

# Apply the configuration to the app
flaskApp.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy()

# Create the database and tables
with flaskApp.app_context():
    db.create_all()

