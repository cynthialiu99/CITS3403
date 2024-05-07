import sqlite3
from flask import redirect, render_template, request, url_for, jsonify
from app import flaskApp
from app.models import Student, Staff

@flaskApp.route("/")

@flaskApp.route('/signup')
def signup():
    return render_template('Sign Up.html')

@flaskApp.route('/signup/submit', methods=['POST'])
def submit():
    print(request.method)
    print(request.form)
    print("Submitted!")
    return redirect(location="/login")

@flaskApp.route('/login', methods=['GET'])
def login():
    return redirect(location="/login/submit")

@flaskApp.route('/login/submit', methods=['POST'])
def submit2():
    print(request.method)
    print(request.form)
    print("Submitted!")
    return redirect(location="/account")

@flaskApp.route('/account', methods=['GET'])
def account():
    return render_template("Account.html")

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

@flaskApp.route('/threads/<thread_id>/reply', methods=['GET'])
def reply_threads():
    return render_template("Reply_Threads.html")

@flaskApp.route('/homepage/python', methods=['GET'])
def python():
    return render_template('PythonHomePage.html')

@flaskApp.route('/homepage/java', methods=['GET'])
def java():
    return render_template('JavaHomePage.html')

@flaskApp.route('/contact', methods=['GET'])
def contact():
    return render_template('ContactUs.html')

if __name__ == '__main__':
    flaskApp.run(debug=True)


