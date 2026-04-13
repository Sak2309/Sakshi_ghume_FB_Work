from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/signin")
def login():
    return render_template("login.html")

@app.route("/verify", methods=["POST"])
def verify():
    #fetch the data using post method
    uname = request.form.get("uname")
    pwd = request.form.get("pwd")
    if uname == 'sakshi' and pwd == '12345':
        return "Login successful"
    else:
        return "Login failed"

if(__name__ == "__main__"):
    app.run() #start the server