from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def homepage1():
    return  render_template("homepage.html")

@app.route("/")
def timestable(num):
    return  render_template("timestable.html",T=int(num))

app.run()