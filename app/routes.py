import sqlite3
from flask import flash, redirect, render_template, request, url_for, jsonify, session
from urllib.parse import urlsplit
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import create_app, db, migrate
from app.blueprint import main
from app.forms import *
from app.models import *
from flask_login import logout_user, login_required
from flask import Blueprint 

# main = Blueprint('main', __name__)


@main.route('/account')
@login_required
def account():
    threads = []
    if current_user.is_anonymous == False:
        user_id = current_user.id
        user = User.query.get(user_id)
        threads = db.session.query(Thread).join(Post).filter(Post.user_id == user_id).all()
        thread_list = []
        if(len(threads) !=0):
            for thread in threads:
                thread_dict = {
                    'thread_id': thread.thread_id,
                    'thread_name': thread.thread_name
                }
            thread_list.append(thread_dict)
        return render_template('Account.html', user=user, threads = thread_list)
    else:
        # Redirect to login page or handle unauthorized access
        return redirect(url_for('main.login'))
    # return render_template("Account.html", title='Account Page')

@main.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.account'))
    
    form = SignUp()
    if form.validate_on_submit():
        form.type.data = "student"
        form.create_user()
        return redirect(url_for('main.login'))
    return render_template('Sign Up (Student).html', title='Sign Up', form=form)

@main.route('/login', methods=['GET','POST'])
def login():
    error = ""
    if current_user.is_authenticated:
        return redirect(url_for('main.account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            error = 'Incorrect Username or Password'
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('main.account')
            return redirect(next_page)
    return render_template('Login.html', title='Sign In', form=form, error = error)

@main.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# Route to create a new thread
@main.route('/create_threads', methods=['GET'])
@login_required
def get_create_threads():
    form = CreateThreadForm()
    return render_template('Create_Threads.html', title = 'Create Thread', form = form)

# Route to create a new thread
@main.route('/create_threads', methods=['POST'])
@login_required
def create_threads():
    form = CreateThreadForm()
    if form.validate_on_submit():
        postid, threadid = form.create_thread(current_user.id)
        return redirect(url_for('main.single_thread', thread_id=threadid))
    return render_template('Create_Threads.html', title = 'Create Thread', form = form)

# Route to retrieve all threads
@main.route('/threads', methods=['GET','POST'])
def get_threads():
    form = Search()
    value = form.search.data
    search = "%{}%".format(value)
    if value == "":
        threads = db.session.query(Thread).all()
    else:
        threads = db.session.query(Thread).filter(Thread.thread_name.like(search)).all()
    return render_template('Display_Threads.html', title = "displaythreads", threads = threads, form = form)

@main.route('/threads/<int:thread_id>', methods=['GET'])
def single_thread(thread_id):
    thread = Thread.query.get_or_404(thread_id)
    responses = Response.query.filter_by(thread_id=thread_id).all()
    responsearray = []
    for response in responses:
        responsearray.append(Post.query.filter_by(id = response.post_id).first())
    return render_template('Single_Thread.html', thread=thread, responses=responsearray, user = current_user)


#Route to reply to threads
@main.route('/threads/<int:thread_id>/reply', methods=['GET'])
def reply_threads(thread_id):
    form = ReplyThreadForm()
    return render_template("Reply_Threads.html", thread_id = thread_id, form = form)

@main.route('/threads/<int:thread_id>/reply', methods=['POST'])
def post_reply_threads(thread_id):
    thread_id = request.view_args['thread_id']
    form = ReplyThreadForm()
    form.reply_thread(current_user.id, thread_id)
    thread = Thread.query.get_or_404(thread_id)
    responses = Response.query.filter_by(thread_id=thread_id).order_by(Response.post.has(Post.timestamp)).all()
    return render_template('Single_Thread.html', thread=thread, response = responses, user = current_user)

@main.route('/homepage/python', methods=['GET'])
def python():
    form = Search()
    return render_template('PythonHomePage.html', form = form)

@main.route('/homepage/java', methods=['GET'])
def java():
    form = Search()
    return render_template('JavaHomePage.html', form = form)

@main.route('/contact', methods=['GET'])
def contact():
    return render_template('ContactUs.html')

@main.route("/")
@main.route('/home', methods=['GET'])
def home():
    return render_template('HomePage.html')

@main.route('/signup_academic', methods=['GET', 'POST'])
def signup_academic():
    if current_user.is_authenticated:
        return redirect(url_for('main.account'))

    form = SignUp()
    if form.validate_on_submit():
        form.type.data = "academic"
        form.create_user()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('Sign Up (Academic Staff).html', title='Sign Up', form=form)

@main.route('/forgot_passwd', methods = ['GET', 'POST'])
def forgot_passwd():
    return render_template('ForgotPassword.html', title ='ForgotPassword')



flaskApp = create_app()

if __name__ == '__main__':
    flaskApp.run(debug=True)
