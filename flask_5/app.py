from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    url_name = request.args.get("URL_KEY_NAME","MATEYS")
    return render_template("index.html",JINJA_NAME=url_name)