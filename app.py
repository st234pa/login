from flask import Flask, render_template, request
import hashlib
import csv

app = Flask(__name__)

def hash(x):
    h = hashlib.sha1()
    h.update(x)
    return h.hexdigest()

def register(username, password):
    d = csv.reader(open("data/d.csv"))
    for i in d:
        if username == i[0]:
            return "You are already registered."
    with open('data/d.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([username, hash(password)])
    return "You are now successfully registered."

def checkLogin(username, password):
    d = csv.reader(open("data/d.csv"))
    for i in d:
        if username == i[0]:
            if i[1] == hash(password):
                return "You are now successfully logged in."
            return "Incorrect password."
    return "Incorrect username."

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
    if response['enter'] == 'Register':
        m1 = register(username, password)
        return render_template("login.html", message = m1)
    else:
        m2 = checkLogin(username, password)
        return render_template("login.html", message = m2)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
