from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
#TODO jak zrobić 

@app.route('/login', methods = ["POST", "GET"])
def login():
    return render_template("login.html")    

@app.route('/registration', methods = ["POST", "GET"])
def registration():
    return f"<h1>Regist Page </h1>"

@app.route("/usr")                                            
def user():
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True)


