import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=None):
    flaskApp = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config:
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "my_secret_key")
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')

    class DeploymentConfig(Config):
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')
    
    class TestConfig(Config):
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        TESTING = True

    if config_class:
        flaskApp.config.from_object(config_class)
    else:
        flaskApp.config.from_object(Config)

    # Initialize the extensions with the app
    db.init_app(flaskApp)
    migrate.init_app(flaskApp, db)
    login.init_app(flaskApp)
    login.login_view = 'main.login'  # Update the login view to match your Blueprint's endpoint

    # Import and register the main Blueprint
    from .blueprint import main as main_blueprint
    flaskApp.register_blueprint(main_blueprint)

    # Ensure models are imported to register them with SQLAlchemy
    with flaskApp.app_context():
        from . import models  # Import models to register them with SQLAlchemy
        db.create_all()  # Create the database tables

    return flaskApp