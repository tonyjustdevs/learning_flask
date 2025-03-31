from flask import Flask, render_template, request

app = Flask(__name__)


SPORTS_ALLOWS = ["Soccer","Swimming","Basketball"]

REGISTRANTS = {}
print(REGISTRANTS)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=['GET','POST']) 
def register():
    # sport_chosen        = request.form.get("sports")
    # first_name_chosen   = request.form.get("firstname")

    sport_chosen        = request.args.get("sports")
    first_name_chosen   = request.args.get("firstname")

    {'key': 'value'}
    print(first_name_chosen,sport_chosen)
    if sport_chosen in SPORTS_ALLOWS:
        # REGISTRANTS["tony"]="soccer"
        REGISTRANTS[first_name_chosen]=sport_chosen
        print(REGISTRANTS)
        
        return render_template("register.html")
    else:
        return render_template("error.html")
    
@app.route("/registrants")  
def registrants():
    # return render_template("registrants.html",REGISTRANTS_DICT_JINJA ="TRAN")
    return render_template("registrants.html",REGISTRANTS_DICT_JINJA =REGISTRANTS)
