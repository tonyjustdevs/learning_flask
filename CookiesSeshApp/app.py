from flask import Flask, request, url_for, render_template, session, make_response
# from flask.sessions import SecureCookieSessionInterface
# from flask_session.sessions import 



app = Flask(__name__, template_folder="templates", static_folder="static")
# app.session_interface 
@app.route("/")
def index():
    return render_template("index.html", server_msg = "G'day Mateys! 🐨🐨🐨")

@app.route("/set_cookie")
def set_cookie_fn():
    server_response = make_response(render_template("index.html", server_msg = "Cookies Set."))
    server_response.set_cookie("tony_cookie_1","cookie_value_1")
    server_response.set_cookie("tony_cookie_2","420")
    server_response.set_cookie("tony_cookie_3_secure","69",secure=True)
    return server_response

@app.route("/get_cookie")
def get_cookie_fn():
    # first_cookie_name = list(request.cookies.keys())[0]
    # first_cookie_value = request.cookies[first_cookie_name]
    # return render_template("index.html", server_msg = f"cookie: {first_cookie_name!r}, cookie_value: {first_cookie_value!r}")
    cookies_values = [(k,v) for k,v in request.cookies.items()]
    return render_template("index.html", server_msg = f"{cookies_values}")

@app.route("/remove_cookies")
def remove_cookies_fn():
    cookies_values = [(k,v) for k,v in request.cookies.items()]

    server_response = make_response(render_template("index.html", server_msg = f"Cookies: {cookies_values}"))

    for cookie_key in request.cookies.keys():
        print(f"deleting cookie: {cookie_key}")
        # server_response.set_cookie(cookie_key,'',expires=0)
        server_response.set_cookie(cookie_key,'',max_age=0)
        # server_response.delete_cookie(cookie_key)

    return server_response



app.secret_key="a_very_good_secret_key"

@app.route("/save_session")
def save_session_fn():
    session["sesh_key_1"] = "sesh_val_1"
    session["sesh_key_2"] = 69
    session["sesh_key_3"] = 420
    print(f"flask default session object: {session}, {type(session)}")
    return render_template("index.html", server_msg = "Session Data Saved.")

@app.route("/get_session")
def get_session_fn():
    return render_template("index.html", 
                           server_msg = f"sesh_key_1: {session.get('sesh_key_1','not set')},  sesh_key_mate: {session.get('sesh_key_mate','not set')}")

@app.route("/clear_session")
def clear_session_fn():
    session.clear()
    return render_template("index.html", 
                           server_msg = f"sesh_key_1: {session.get('sesh_key_1','not set')},  sesh_key_mate: {session.get('sesh_key_mate','not set')}")

@app.route("/delete_a_cookie", methods=["GET","POST"])
def delete_a_cookie_fn():
    print(request.method)
    if request.method == "GET":
        print(f"cookie_to_delete: {request.args}")
        if request.cookies.keys():
            keys_list = list(request.cookies) # get cookies keys
            print(keys_list, type(keys_list))
            return render_template("index.html",
                                   KEYS_LIST = keys_list,
                                   server_msg="Deciding which cookie to delete...")
        else:
            return render_template("index.html", "dont think this ever prints")
    else:
        if request.method == "POST":
            cookie_to_delete = list(request.form.values())[0]
            print(f"cookie_to_delete: {cookie_to_delete}") 
            # request.cookies.delete_cookie(cookie_to_delete)
            # Why list(...) then [0]? because .values() is a dict generator, convert into a list
            
            server_response = make_response(render_template("index.html", server_msg = f"Cookies deleted: {cookie_to_delete}"))
            server_response.set_cookie(cookie_to_delete,'',max_age=0)

            return server_response
            
@app.route("/set_a_cookie", methods=["GET","POST"])
def set_a_cookie_fn():
    print(request.method)
    if request.method == "GET":
        return render_template("index.html", server_msg ="Trying to set a cookie...🍪", SETACOOKIE="Set a cookie")
    else:
        new_cookies = list(request.form.items())
        server_response = make_response(render_template("index.html", server_msg = f"Set A Cookie...🥠: {new_cookies}"))
        
        # for k,v in request.form.items():
            
        # print(new_cookies)
        return server_response
        



if __name__ == "__main__":
    app.run("0.0.0.0",port=5000,debug=True)
    