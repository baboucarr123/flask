from flask import Flask, render_template

app=Flask(__name__)

@app.route("/info1")
def homepage1():
    return  render_template("information.html", na="babs", addr="london",color="green")

@app.route("/info2")
def homepage():
    return  render_template("information.html", na="babs", addr="london", color="red")
    
@app.route("/info3")
def homepage2():
    return  render_template("information.html", na="babs", addr="london",color="blue")

app.run()

