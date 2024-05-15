import sqlite3
from flask import flash, redirect, render_template, request, url_for, jsonify
from urllib.parse import urlsplit
from flask_login import current_user, login_user
import sqlalchemy as sa
from blueprint import main
from app import db, flaskApp
from app.forms import SignUp, LoginForm
from app.models import User
from flask_login import logout_user, login_required

@main.route('/account')
#@login_required
def account():
    user = {'username': 'SupremeLord'}
    return render_template("Account.html", title='Account Page')

@main.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.account'))
    
    form = SignUp()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('Sign Up (Student).html', title='Sign Up', form=form)

@main.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.account')
        return redirect(next_page)
    return render_template('Login.html', title='Sign In', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.signup'))

# Route to create a new thread
@main.route('/threads', methods=['POST'])
def create_thread():
    data = request.json
    conn = sqlite3.connect('threads.db')
    c = conn.cursor()
    c.execute('''INSERT INTO threads (title, content, date) VALUES (?, ?, ?)''', (data['title'], data['content'], data['date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Thread created successfully'}), 201

# Route to retrieve all threads
@main.route('/threads', methods=['GET'])
def get_threads():
    conn = sqlite3.connect('threads.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM threads''')
    threads = c.fetchall()
    conn.close()
    return jsonify(threads), 200

#Route to reply to threads
@main.route('/threads/<thread_id>/reply', methods=['GET'])
def reply_threads():
    return render_template("Reply_Threads.html")

@main.route('/homepage/python', methods=['GET'])
def python():
    return render_template('PythonHomePage.html')

@main.route('/homepage/java', methods=['GET'])
def java():
    return render_template('JavaHomePage.html')

@main.route('/contact', methods=['GET'])
def contact():
    return render_template('ContactUs.html')

if __name__ == '__main__':
    flaskApp.run(debug=True)

@main.route("/")
@main.route('/home', methods=['GET'])
def home():
    return render_template('HomePage.html')

@main.route('/signup_academic', methods=['GET', 'POST'])
def signup_academic():
    return render_template('Sign Up (Academic Staff).html', title='Sign Up Staff')

@main.route('/forgot_passwd', methods = ['GET', 'POST'])
def forgot_passwd():
    return render_template('ForgotPassword.html', title ='ForgotPassword')
