from flask import Flask, render_template, request

import sys
print()
print("Intepreter:\t", sys.executable)
print("Full-Path:\t", __file__,"|",sys.argv[0],"| args:",sys.argv[1:])
print("Py-Vers:\t",sys.version,"|", sys.platform) 
print()

 
app = Flask(__name__)


@app.route("/")
def index(): ##### Version 2: Process URL Query Parameters
    url_key_name_str = request.args.get('URL_KEY_NAME',"default 🐈")
    return render_template("index.html", JINJA_NAME = url_key_name_str)

@app.route("/greet")
def greet():
    url_key_name_str = request.args.get("URL_KEY_NAME","🐶")
    return render_template("greet.html", JINJA_NAME = url_key_name_str)

# if True:  # exit program early (optional status code)
#     sys.exit(0) #0: success !0: error  
    # print("Modules:",sys.modules.keys())  # Lists all loaded modules
    # print("ModulePaths:",sys.path)  # Shows Python module search paths
    # print("VersInfo:",sys.version_info) # Tuple (major, minor, micro, releaselevel, serial)
    # import sysconfig
    # print("SConfigsPaths: ",sysconfig.get_paths())