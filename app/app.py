import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

flaskApp = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

flaskApp.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flaskApp)
