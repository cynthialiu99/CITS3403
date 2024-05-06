import sqlite3

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