from flask import Flask, render_template, redirect, request, session, url_for
from datetime import datetime

app = Flask(__name__, template_folder="templates", static_folder="static",
            static_url_path="/")

app.secret_key="not_the_greatest_secret_key"

@app.route("/")
def index_fn():
    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time = "2025-04-07 12:55:00"
    return render_template("index.html", server_msg = f"G'day Mateys 🙋‍♂️ (Last Saved By Tony: [{current_time} (Indochina Time, ICT)])")

@app.route("/set_session_data")
def set_session_data_fn():
    session["name"] = "tony"
    session["value"] = 69
    return render_template("index.html", server_msg = "Session Data Set.")

@app.route("/get_session_data")
def get_session_data_fn():
    if "name" in session:
        session_name = session["name"]
        session_value = session["value"] 
        return render_template("index.html", server_msg = f"name: {session_name}, value: {session_value}.")
    else:
        return render_template("index.html", server_msg = f"No Session Data.")
        
@app.route("/clear_session_data")
def clear_session_data_fn():
    session.clear()
    return render_template("index.html", server_msg = "Session Cleared.")

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000,debug=False)
    