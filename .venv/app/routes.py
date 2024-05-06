import sqlite3
from flask import redirect, render_template, request, url_for, jsonify
from app import flaskApp
from app.models import Student, Staff

@flaskApp.route("/")

@flaskApp.route('/signup')
def signup():
    return render_template('Sign Up.html')
    
@flaskApp.route('/submit', methods=['post'])
def submit():
    print(request.method)
    print(request.form)
    print("Submitted!")
    return redirect(location="Login.html")

# Function to create the SQLite database
def create_db():
    conn = sqlite3.connect('threads.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS threads
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, date TEXT)''')
    conn.commit()
    conn.close()

# Call the create_db() function to create the database
create_db()

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

if __name__ == '__main__':
    flaskApp.run(debug=True)


