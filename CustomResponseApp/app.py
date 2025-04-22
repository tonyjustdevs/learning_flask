from flask import Flask, render_template, request, make_response


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", SERVER_MSG = "G'day Mateys 🦘!")

def add_cookies_fn():
    make_response()
    
    return render_template("index.html", SERVER_MSG = "Cookies Added 🍪!")

def get_cookies_fn():
    return ""

def delete_cookies_fn():
    return ""

def save_session_fn():
    return ""

def get_session_fn():
    return ""

def delete_session_fn():
    return ""


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)