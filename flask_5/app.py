from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def index(): ##### Version 1: does not process url args key vals  #####
#     return render_template("index.html")

@app.route("/")
def index(): ##### Version 2: Process URL Query Parameters
    # print(request.args, type(request.args)) 
    #   ImmutableMultiDict([('URL_KEY_NAME', 'mate')]) <class 'werkzeug.datastructures.structures.ImmutableMultiDict'>
    # print("URL_KEY_NAME", request.args['URL_KEY_NAME'], type(request.args['URL_KEY_NAME']), len(request.args)) 
    #   URL_KEY_NAME matematemate <class 'str'> 1
    url_key_name_str = request.args.get('URL_KEY_NAME',"default 🐈")
    print(url_key_name_str)
    return render_template("index.html", JINJA_NAME = url_key_name_str)
    # return render_template("index.html", JINJA_NAME = None)