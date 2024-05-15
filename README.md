
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


### Installing Packages and Running flask

To setup the virtual environment and run flask, open the root directory of the project in a terminal and type:

(Using Windows Command Prompt)

```
$ python3 -m venv venv
$ venv\Scripts\activate
$ pip install flask
$ pip install flask_sqlalchemy
$ pip install flask_migrate
$ pip install flask_login
$ pip install wtforms
$ pip install flask_wtf
$ pip install selenium
$ set FLASK_APP = projectify.py 
$ flask run
```
For linux/mac use these commands instead of venv\Scripts\activate and set FLASK_APP = projectify.py:
```
$ source venv/bin/activate
$ export FLASK_APP=projectify.py
```
For windows powershell, use this command instead of venv\Scripts\activate:

```
$venv\Scripts\Activate.ps1
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

### Dependencies -> requirements.txt file
alembic==1.13.1
blinker==1.8.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
Flask-Login==0.6.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
greenlet==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.3
MarkupSafe==2.1.5
SQLAlchemy==2.0.30
typing_extensions==4.11.0
Werkzeug==3.0.3
WTForms==3.1.2


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
