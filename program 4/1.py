from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("inputform.html")

@app.route("/data", methods=["POST"])
def process():
    print(request.form)
    print("helloooooooooooooooooooooooooooo")
    print(request.form["num1"])
    A=int(request.form["num1"])
    B=int(request.form["num2"])
    print(A,B)
    return render_template("timestable.html",T=A, R=B)

app.run(debug=True)