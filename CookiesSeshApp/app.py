from flask import Flask, request, url_for, render_template, session, make_response

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html", server_msg = "G'day Mateys! 🐨🐨🐨")
    # return render_template("index2.html")

@app.route("/set_cookie")
def set_cookie_fn():
    server_response = make_response(render_template("index.html", server_msg = "Cookies Set."))
    server_response.set_cookie("coolcookie","youare")
    return server_response

@app.route("/get_cookie")
def get_cookie_fn():
    first_cookie_name = list(request.cookies.keys())[0]
    first_cookie_value = request.cookies[first_cookie_name]
    # print(keys_list[0], cookie_value) # dict_keys(['coolcookie']) <generator object MultiDict.values at 0x7f714dfa1150>
    return render_template("index.html", server_msg = f"cookie: {first_cookie_name!r}, cookie_value: {first_cookie_value!r}")


if __name__ == "__main__":
    app.run("0.0.0.0",port=5000,debug=True)
    


