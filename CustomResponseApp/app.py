from flask import Flask, render_template, request, make_response, jsonify, session, url_for


app = Flask(__name__)
app.secret_key = "a_very_not_secret_key"

@app.route("/")
def index():
    server_response = make_response(render_template("index.html", SERVER_MSG = "G'day Mateys 🦘!"))
    return server_response

@app.route("/tony1")
def tony1():
    return render_template("index.html", SERVER_MSG = "Returned default render_template()")

@app.route("/tony2")
def tony2():
    rendered = render_template("index.html", SERVER_MSG = "Returned make_response(...)")
    server_response = make_response(rendered)
    
    server_response.headers["TP_Header_1"] = "mate"
    server_response.headers["TP_Header_2"] = 420
    
    server_response.set_cookie("TP_Cookie_1","69")
    server_response.set_cookie("TP_Cookie_2","666")
    
    debug_info = {
        'status':   server_response.status,
        'headers':  dict(server_response.headers),
        'body':     server_response.get_data(as_text=True),
        'cookies':  server_response.headers.getlist("Set-Cookie")
    }
    
    # print(debug_info)
    # return jsonify(debug_info)
    return server_response


def add_cookies_fn():
    make_response()
    
    return render_template("index.html", SERVER_MSG = "Cookies Added 🍪!")

# def get_cookies_fn():
#     return ""

# def delete_cookies_fn():
#     return ""

@app.route("/save_session")
def save_session_fn():
    session["user_session_key_1"] = "user_session_val_1"
    return render_template("index.html", SERVER_MSG = "Session Saved 🗃️!")

# def get_session_fn():
#     return ""

# def delete_session_fn():
#     return ""


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)