from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# [input]  add (input_text): takes name from user
# [output] (alert) popup in browse