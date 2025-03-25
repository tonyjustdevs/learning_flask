from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index(): ##### Version 2: Process URL Query Parameters
    url_key_name_str = request.args.get('URL_KEY_NAME',"default 🐈")
    return render_template("index.html", JINJA_NAME = url_key_name_str)

@app.route("/greet")
def greet():
    url_key_name_str = request.args.get("URL_KEY_NAME","🐶")
    return render_template("greet.html", JINJA_NAME = url_key_name_str)

# @app.route("/")
# def index(): ##### Version 1: does not process url args key vals  #####
#     return render_template("index.html")

    # print(request.args, type(request.args)) 
    #   ImmutableMultiDict([('URL_KEY_NAME', 'mate')]) <class 'werkzeug.datastructures.structures.ImmutableMultiDict'>
    # print("URL_KEY_NAME", request.args['URL_KEY_NAME'], type(request.args['URL_KEY_NAME']), len(request.args)) 
    #   URL_KEY_NAME matematemate <class 'str'> 1
    # return render_template("index.html", JINJA_NAME = None)