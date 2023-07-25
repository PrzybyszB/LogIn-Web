from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app)

class users(db.Model): 
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable = False)
    # email = db.Column (db.String(100), nullable = False)
    # password = db.Column (db.String(100), nullable = False)
    # date_created = db.Column(db.DateTime, default = datetime.utcnow)


    def __init__(self, name):
        self.name = name



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":                             
        user = request.form["login"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")
            

@app.route("/<usr>")                                            
def user(usr):
    return render_template("user.html", user = usr)


    
@app.route('/registration', methods = ["POST", "GET"])
def registration():
    if request.method == "POST" and "r_login" in request.form and "password" in request.form and "email" in request.form:                             
        r_user = request.form["r_login"]
        # password = request.form["password"]
        # email = request.form["email"]
        # found_user = users.query.filter_by(name=r_user).first()
        r_usr = users(r_user)
        db.session.add(r_usr)
        db.session.commit()

        return redirect(url_for("r_user", r_usr = r_user))
    else:
        user_list = users.query.order_by(users._id)
        return render_template("registration.html", user_list = user_list)

#czemu tutaj bez nakierowanie /r_user strona nie przekierowuje tam a w user zwyklym to dziala

@app.route("/r_user/<r_usr>")                                            
def r_user(r_usr):
    return render_template("r_user.html", r_user = r_usr)





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



#TODO DB ogarnac z rejestracja i logownaiem
