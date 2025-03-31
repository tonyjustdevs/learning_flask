from flask import Flask, render_template,request, redirect, session
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    # name = None
    name = "Messi"
    return render_template("index.html", JINJA_NAME = name) 

 
#NOW 
#78 add logout anchor link to logout route if user is loggedin
#77 add login anchor link to login route if user logged out to index.html    less than a minute ago