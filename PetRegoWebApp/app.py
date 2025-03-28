from flask import Flask, render_template

app = Flask(__name__)

print("yo")

@app.route("/")
def index():
    return render_template("index.html")