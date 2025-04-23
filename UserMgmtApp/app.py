from flask import Flask, request, redirect, url_for, session, render_template_string, flash
from flask_session import Session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a secure random key in production
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DB_NAME = 'users.db'

# Initialize DB
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
init_db()

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            flash("User registered successfully!", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.", "error")
    return render_template_string('''
        <h2>Register</h2>
        <form method="POST">
            Username: <input name="username" required><br>
            Password: <input name="password" type="password" required><br>
            <button type="submit">Register</button>
        </form>
        <a href="{{ url_for('login') }}">Login</a>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% for category, message in messages %}
            <p style="color: {% if category == 'error' %}red{% else %}green{% endif %}">{{ message }}</p>
          {% endfor %}
        {% endwith %}
    ''')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        with sqlite3.connect(DB_NAME) as conn:
            user = conn.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password)).fetchone()
            if user:
                session['username'] = username
                flash("Logged in successfully!", "success")
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials", "error")
    return render_template_string('''
        <h2>Login</h2>
        <form method="POST">
            Username: <input name="username" required><br>
            Password: <input name="password" type="password" required><br>
            <button type="submit">Login</button>
        </form>
        <a href="{{ url_for('register') }}">Register</a>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% for category, message in messages %}
            <p style="color: {% if category == 'error' %}red{% else %}green{% endif %}">{{ message }}</p>
          {% endfor %}
        {% endwith %}
    ''')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_NAME) as conn:
        users = conn.execute('SELECT id, username FROM users').fetchall()

    return render_template_string('''
        <h2>Welcome, {{ session['username'] }}</h2>
        <a href="{{ url_for('logout') }}">Logout</a><br><br>
        <h3>Registered Users</h3>
        <ul>
            {% for user_id, username in users %}
                <li>{{ username }}
                    {% if username != session['username'] %}
                        - <a href="{{ url_for('delete_user', user_id=user_id) }}">Delete</a>
                    {% endif %}
                </li>
            {% endfor %}
        </ul>
    ''', users=users)

# Delete User
@app.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM users WHERE id=? AND username != ?', (user_id, session['username']))
    flash("User deleted (if not yourself).", "success")
    return redirect(url_for('dashboard'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Run app
if __name__ == '__main__':
    app.run(debug=True)
