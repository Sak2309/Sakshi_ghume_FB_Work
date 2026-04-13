from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/displayname")
def displayname():
    name="Sakshi ghume"
    return render_template("displayname.html", uname=name)

@app.route("/displaynames")
def displaynames():
    firstname="Sakshi"
    secondname="ghume"
    return render_template("displaynames.html",firstname=firstname, secondname=secondname)

@app.route("/displaylist")
def displaylist():
    data = ["Sakshi", "saniya", "riya","priya","isha"]
    return render_template("displaylist.html", data=data)

@app.route("/displaynestedlist")
def displaynestedlist():
    data = [
        [101,"Sakshi", 88],
        [102,"saniya", 92],
        [103,"riya", 85],
        [104,"priya", 90],
        [105,"isha", 87]
    ]
    return render_template("displaynestedlist.html", data=data)     

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form.get("uname")
    pwd = request.form.get("pwd")
    if uname == 'sakshi' and pwd == '12345':
        return "Login successful"
    else:
        return "Login failed"

    
    

if(__name__ == "__main__"):
    app.run() #start the server
