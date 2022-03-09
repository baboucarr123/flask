from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/page2/<T>")
def page2(T):
    return render_template("page2.html",timestable=T)

@app.route("/page3/<T>/<R>")
def page3(T,R):
    return render_template("timestable.html",timestable=int(T),Range=int(R))

app.run(debug=True)