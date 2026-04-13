from flask import Flask, render_template

app = Flask(__name__)

@app.route("/signin")
def login():
    return render_template("login.html")

@app.route("/verify")
def verify():
    return "I an verify method , i will verify login credential"

@app.route("/signup")
def register():
    return "This is the register method"

if(__name__ == "__main__"):
    app.run() #start the server
deu-hqnp-yxf