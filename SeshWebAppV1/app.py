from flask import Flask, render_template,request, redirect, session
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    name = None
    # name = "messi"
    return render_template("index.html", JINJA_NAME = name) #NOW add jinja if logic