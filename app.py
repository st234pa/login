from flask import Flask, render_template, request, session
import hashlib
import csv

app = Flask(__name__)
#SESSION_TYPE = 'redis'
#app.config.from_object(__name__)
#Session(app)
app.secret_key = '??_|??0??l6?J??8?J2????A???+q? '

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
                session[username] = hash(password)
                return "You are now successfully logged in."
            return "Incorrect password."
    return "Incorrect username."

@app.route("/")
def root():
    return redirect(url_for('login'))

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
