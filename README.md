
# CITS3403 Project
CITS3403 CodeCentral (Student Help Forum)
This is a project submission for CITS3403 (Agile Web Development) at UWA (The University of Western Australia) by Sia Dubey, Cynthia Liu, Neha Menon, Vinita Rathore

## Description

The idea of this app is a simple UWA student help forum where the students can submit posts and tutors can reply to their queries. Students and Staff will be able to register and keep track of their points which are earned through the number of posts and replies they submit.

## Getting Started

These instructions will get you started to playing and navigating throughout the application. It will also serve as a guide to ensure that the project is up and running on your local machine with minimal problems.

### Prerequisites

A minimum of python 3.8 is required to run this project

on Mac:

```
brew install python3
```

On Linux:

```
sudo apt-get install python3.6
```

For windows, download the installer from python's website

```
https://www.python.org/downloads/
```


### Installing and Running flask

To setup the virtual environment and run flask using Windows, open the root directory of the project in a terminal and type:

```
$ python3 -m venv venv
$ venv\Scripts\activate
$ pip install flask
$ pip install flask_sqlalchemy
$ pip install flask_migrate
$ pip install flask_login
$ pip install wtforms
$ pip install flask_wtf
$ set FLASK_APP = projectify.py 
$ flask run
```

### Testing

To run the system tests, on the main directory, open a terminal and run:

```
python -m unittest tests/system_test.py
```

To run the unit tests, run:

```
python -m unittest tests/unit_test.py
```


### Dummy Accounts

There are Pre existing accounts that have been created for the user to use:

Student User:
* Username: 8 digit number
* Email: Username@student.uwa.edu.au

Staff User:
* Username: 8 digit number
* Email: Username@uwa.edu.au

### Dependencies

* alembic==1.5.8
* asgiref==3.5.0
* astroid==2.5.6
* autopep8==1.5.7
* Babel==2.9.1
* bcrypt==3.2.0
* blinker==1.4
* cffi==1.15.0
* click==8.1.2
* cryptography==37.0.2
* dnspython==2.2.1
* dominate==2.6.0
* email-validator==1.1.3
* Flask==2.1.1
* Flask-Admin==1.6.0
* Flask-Bcrypt==1.0.1
* Flask-Bootstrap==3.3.7.1
* Flask-Cors==3.0.10
* Flask-Login==0.6.0
* Flask-Mail==0.9.1
* Flask-Migrate==3.1.0
* Flask-SQLAlchemy==2.5.1
* Flask-User==1.0.2.2
* Flask-WTF==1.0.1
* greenlet==1.1.2
* idna==3.3
* importlib-metadata==4.11.3
* importlib-resources==5.7.1
* is-disposable-email==1.0.0
* itsdangerous==2.1.2
* Jinja2==3.1.1
* lazy-object-proxy==1.6.0
* Mako==1.1.4
* MarkupSafe==2.1.1
* passlib==1.7.4
* pycodestyle==2.7.0
* pycparser==2.21
* python-dateutil==2.8.1
* python-dotenv==0.20.0
* python-editor==1.0.4
* pytz==2021.1
* six==1.16.0
* SQLAlchemy==1.4.35
* sqlparse==0.4.2
* toml==0.10.2
* visitor==0.1.3
* Werkzeug==2.1.1
* wrapt==1.12.1
* WTForms==3.0.1
* wtforms-validators==1.0.0
* zipp==3.8.0

## Built With

* Flask - web framework used
* Python - packages and dependency management 
* Bootstrap - Styling of front end development
* HTML - Creating webpage templates
* CSS - Designing and styling webpages
* JavaScript, JQuery, AJAX - Adding functionality and making dynamic webpages
* Websockets - used for testing files 
* SQLite (accessed via the SQLAlchemy package) - used to create database

## Group Members

| Student Names | Student ID    | GitHub Username |
| ------------- |---------------| ----------------|
| Sia Dubey     | 23066191      |  sdubey2024     |
| Cynthia Liu   | 23387046      |  cynthialiu99   |
| Neha Menon    | 23516355      |  nehamenon139   |
| Vinita Rathore| 23147456      |  vinita254      |
