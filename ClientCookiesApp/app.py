from flask import Flask, request, redirect, render_template
from flask_session import Session

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")

@app.route("/")
def index():
    
    return render_template("index.html")

app.run(host = "0.0.0.0",debug=False)

# pip-compile requirements.in --output-file requirements.txt  # Creates a pinned `requirements.txt`
# pip download -r requirements.txt -d ./offline_packages
# copy requirements.txt (the pinned dependencies) to offline_machine
# copy ./offline_packages (the downloaded wheels) to offline_machine

# pip install --no-index --find-links=./offline_packages -r requirements.txt
# pip-sync --no-index --find-links=./offline_packages requirements.txt
# pip-sync requirements.txt --no-index --find-links=packages
# --no-index: means offline
# --find-links: directory of offline whls