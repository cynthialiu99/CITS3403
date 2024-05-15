from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)

db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)
login = LoginManager(flaskApp)
login.login_view = 'login'



db = SQLAlchemy()
def create_app(config):
    flaskApp = Flask(__name__)
    flaskApp.config.from_object(Config)
    #intialise routes
    db.init_app(flaskApp)

    from app.blueprint import main
    flaskApp.register_blueprint(main)


    return flaskApp

from app import models, routes