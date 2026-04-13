from flask import Flask#,render_template

app = Flask(__name__)

@app.route("/signin")
def login():
    return "i am login function"
    #return render_template("login.html")
@app.route("/signin")
def register():
    return "i am register function"

if(__name__=="__main__"):
   app.run
