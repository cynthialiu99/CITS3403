import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config, DeploymentConfig, TestConfig  # Import the configurations

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    flaskApp = Flask(__name__)

    flaskApp.config.from_object(config_class)

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
