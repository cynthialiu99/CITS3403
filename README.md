
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
$ pip install -r requirements.txt
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
attrs==23.2.0
blinker==1.8.2
certifi==2024.2.2
cffi==1.16.0
click==8.1.7
colorama==0.4.6
dnspython==2.6.1
email_validator==2.1.1
exceptiongroup==1.2.1
Flask==3.0.3
Flask-Login==0.6.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
greenlet==3.0.3
h11==0.14.0
idna==3.7
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.5
MarkupSafe==2.1.5
outcome==1.3.0.post0
pycparser==2.22
PySocks==1.7.1
selenium==4.21.0
sniffio==1.3.1
sortedcontainers==2.4.0
SQLAlchemy==2.0.30
trio==0.25.1
trio-websocket==0.11.1
typing_extensions==4.11.0
urllib3==2.2.1
Werkzeug==3.0.3
wsproto==1.2.0
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

## References
Code Central's logo was generated using Wix's Logo Maker - https://www.wix.com/logo/maker
The Flask Mega Tutorial: 
Chapter 1 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
Chapter 2 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
Chapter 3 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
Chapter 4 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
Chapter 5 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
Chapter 6 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars
Chapter 7 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
Chapter 8 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers


