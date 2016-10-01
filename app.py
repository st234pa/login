from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def hash(x):
    return hashlib.sha256(x.encode())

def register(username, password):
    return "You are now successfully registered."

def checkLogin(username, password):
    return "You are now successfully logged in."

@app.route("/")
@app.route("/login/") #multiple routes go to the same function/
def login():
    print request.headers
    return render_template("login.html")
        
@app.route("/authenticate/", methods=['GET', 'POST'])
def auth():
    response = request.form
    username = response['user']
    password = response['password']
    if response['submit'] == 'Register':
        m1 = register(username, password)
        return render_template("login.html", message = m1)
    else:
        m2 = checkLogin(username, password)
        return render_template("login.html", message = m2)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
