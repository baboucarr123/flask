from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
    return ".<h1> <u> Welcome to my homepage </U> </hl>"

@app.route("/aboutus")
def message ():
    return "hello my friends"

@app.route("/nbs")
def boom ():
    return "welcome to NBS"

app.run()