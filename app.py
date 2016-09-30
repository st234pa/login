from flask import Flask, render_template, request
app = Flask(__name__)
example = {"user": "steph", "password": "yoon"}
@app.route("/")
@app.route("/login/") #multiple routes go to the same function/
def login():
    print request.headers
    return render_template("login.html")
@app.route("/authenticate/", methods=['GET', 'POST'])
def auth():
    response = request.form
    if response["user"] == example["user"] and response["password"] == example["password"]:
        return "You have successfully logged in"
    return "Nope"
if __name__ == "__main__":
    app.debug = True
    app.run()
