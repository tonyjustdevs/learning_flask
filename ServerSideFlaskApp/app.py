from flask import Flask, session, redirect, url_for, request, render_template
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'a_super_secret_key'
app.config['SESSION_TYPE'] = 'filesystem' # 🗂️ Flask-Session config (server-side session using disk)
app.config['SESSION_FILE_DIR'] = './flask_sessions'  # or use tempfile.gettempdir()
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# app.permanent_session_lifetime = timedelta(seconds=5)
Session(app) # 


@app.route('/')
def index():
    if session.get('username'):
        username = session.get('username') 
        return render_template("index.html", SERVER_MSG = f"Welcome back, {username}\n", USERNAME=username)
    else: 
        return render_template("index.html", SERVER_MSG = f"Please login")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html", SERVER_MSG = "Logged out!")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        return render_template("index.html", SERVER_MSG = f"Logged in as, {username}", USERNAME=username)
    else:
        if session["username"]:
            return render_template("index.html", SERVER_MSG = f'Welcome back, {username}', USERNAME=username)
        else:
            return render_template("index.html", SERVER_MSG = f'Please login')
            

ALL_USERS = {}

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method=="POST":
        username = request.form("username")
        if username in ALL_USERS:
            return render_template("index.html", SERVER_MSG = f'{username} Already Exists!')
        else:
            return render_template("index.html", SERVER_MSG = f'{username} Registered!')
    else:
        return render_template("index.html", SERVER_MSG = f'Register')
        

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
