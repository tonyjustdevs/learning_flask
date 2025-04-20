from flask import Flask, render_template, make_response, url_for, session, request


app = Flask(__name__)
session(app)
app.config["PERMANENT_SESSION"]=False   

@app.route("/")
def index():
    server_msg = "Reached Default Homepage💤"
    return render_template("index.html", SERVER_MSG=server_msg)


@app.route("/set_cookie")
def set_cookie_fn():
    server_msg = "Cookie has been set!"
    server_response = make_response(render_template("index.html", SERVER_MSG=server_msg))
    server_response.set_cookie("tp_cookie_name","tp_cookie_value", secure=True)
    server_response.set_cookie("tp_cookie_position","69", secure=True)
    return server_response

@app.route("/get_cookie")
def get_cookie_fn():
    cookies_dict = request.cookies.items()
    # for k,v in request.cookies.items():
    #     print(k,v)
        
    server_msg = f"Cookie Names & Cookie Values:"
    return render_template("index.html", SERVER_MSG=server_msg, COOKIES = cookies_dict)

@app.route("/del_cookie")
def del_cookie_fn():
    server_msg = "Cookies Removed! 🚽"
    server_response = make_response(render_template("index.html", SERVER_MSG=server_msg))
    
    # set all cookies to expires 0
    for cookie in request.cookies:
        print(f"Deleteing: {cookie}")
        server_response.set_cookie(cookie,expires=0)
    return server_response

app.secret_key="not_a_great_secret_key"

@app.route("/set_session_client")
def set_session_client_fn():
    server_msg = "Set Client Session."
    session["CLIENT_SESSION_cookie1"] = "420"
    session["CLIENT_SESSION_cookie2"] = "69"
    return render_template("index.html", SERVER_MSG=server_msg)

@app.route("/get_session_client")
def get_session_client_fn():
    server_msg = "Get Client Session Data."
    # session
    # <SecureCookieSession {'CLIENT_SESSION_cookie1': '420', 'CLIENT_SESSION_cookie2': '69'}> <class 'werkzeug.local.LocalProxy'>
    print(session, type(session))
    return render_template("index.html", SERVER_MSG=server_msg, COOKIES = session)

if __name__ == "__main__":
    app.run('0.0.0.0',port=5000,debug=True)