import sqlite3
from flask import flash, redirect, render_template, request, url_for, jsonify
from urllib.parse import urlsplit
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db, flaskApp
from app.forms import SignUp, LoginForm
from app.models import User
from flask_login import logout_user, login_required
from flask import session 

@flaskApp.route('/account')
#@login_required
def account():
    if current_user.is_anonymous == False:
        user_id = current_user.id
        user = User.query.get(user_id)
        return render_template('account.html', user=user)
    else:
        # Redirect to login page or handle unauthorized access
        return redirect(url_for('login'))
    # return render_template("Account.html", title='Account Page')

@flaskApp.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    
    form = SignUp()
    if form.validate_on_submit():
        form.type.data = "student"
        form.create_user()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('Sign Up (Student).html', title='Sign Up', form=form)

@flaskApp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if (user.check_password(form.password.data)) == False:
            flash('Incorrect Username or Password')
            return render_template('Login.html', title='Sign In', form=form)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('account')
        return redirect(next_page)
    return render_template('Login.html', title='Sign In', form=form)

@flaskApp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route to create a new thread
@flaskApp.route('/threads', methods=['POST'])
def create_thread():
    data = request.json
    conn = sqlite3.connect('threads.db')
    c = conn.cursor()
    c.execute('''INSERT INTO threads (title, content, date) VALUES (?, ?, ?)''', (data['title'], data['content'], data['date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Thread created successfully'}), 201

# Route to retrieve all threads
@flaskApp.route('/threads', methods=['GET'])
def get_threads():
    conn = sqlite3.connect('threads.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM threads''')
    threads = c.fetchall()
    conn.close()
    return jsonify(threads), 200

#Route to reply to threads
@flaskApp.route('/threads/<thread_id>/reply', methods=['GET'])
def reply_threads():
    return render_template("Reply_Threads.html")

@flaskApp.route('/home/python', methods=['GET'])
def python():
    return render_template('PythonHomePage.html')

@flaskApp.route('/home/java', methods=['GET'])
def java():
    return render_template('JavaHomePage.html')

@flaskApp.route('/contact', methods=['GET'])
def contact():
    return render_template('ContactUs.html')

@flaskApp.route("/")
@flaskApp.route('/home', methods=['GET'])
def home():
    return render_template('HomePage.html')

@flaskApp.route('/signup_academic', methods=['GET', 'POST'])
def signup_academic():
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    form = SignUp()
    if form.validate_on_submit():
        form.type.data = "academic"
        form.create_user()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('Sign Up (Academic Staff).html', title='Sign Up', form=form)

@flaskApp.route('/forgot_passwd', methods = ['GET', 'POST'])
def forgot_passwd():
    return render_template('ForgotPassword.html', title ='ForgotPassword')

if __name__ == '__main__':
    flaskApp.run(debug=True)
