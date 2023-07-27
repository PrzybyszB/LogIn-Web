from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user, UserMixin, LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hashinshin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
login_manager = LoginManager(app)

db = SQLAlchemy(app)

class users(db.Model, UserMixin): 
    u_id = db.Column("id", db.Integer, primary_key=True)
    r_user = db.Column (db.String(100), nullable = False)
    email = db.Column (db.String(100), nullable = False)
    password = db.Column (db.String(100), nullable = False)


    def __init__(self, email, password, r_user):
        self.email = email
        self.password = password
        self.r_user = r_user
    
    def get_id(self):
        return(self.u_id)
    
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST": 
        email = request.form.get('email')
        password = request.form.get('password')                            
        user = users.query.filter_by(email=email).first()
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")
            

@app.route("/<usr>")                                            
def user(usr):
    return render_template("user.html", user = usr)


    
@app.route('/registration', methods = ["POST", "GET"])
def registration():
    if request.method == "POST":
        r_user = request.form.get("r_login")
        password = request.form.get("password")
        email = request.form.get("email")
        user = users.query.filter_by(email=email).first()
        new_user = users(email=email, r_user = r_user, password=password)

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember = True)
        return redirect(url_for("r_user", r_usr = r_user))
    else:

        return render_template("registration.html", user=current_user)

#czemu tutaj bez nakierowanie /r_user strona nie przekierowuje tam a w user zwyklym to dziala

@app.route("/r_user/<r_usr>")                                            
def r_user(r_usr):
    return render_template("r_user.html", r_user = r_usr)





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



#TODO naprawic Missing user_loader or request_loader. Refer to http://flask-login.readthedocs.io/#how-it-works for more info.
