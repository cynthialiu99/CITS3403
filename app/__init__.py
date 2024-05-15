import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    flaskApp = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config:
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "my_secret_key")
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')

    flaskApp.config.from_object(Config)

    db.init_app(flaskApp)
    migrate.init_app(flaskApp, db)
    login.init_app(flaskApp)
    login.login_view = 'auth.login'

    with flaskApp.app_context():
        from . import models  # Import models to register them with SQLAlchemy
        db.create_all()  # Create the database tables

    from app.blueprint import main as main_blueprint
    flaskApp.register_blueprint(main_blueprint)

