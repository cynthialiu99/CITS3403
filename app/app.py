import os
from app import models
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand

flaskApp = Flask(__name__)
flaskApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

basedir = os.path.abspath(os.path.dirname(__file__))

flaskApp.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flaskApp)
#migrate = Migrate(flaskApp, db)

#manager = Manager(flaskApp)
#manager.add_command('db', MigrateCommand)