from flask import Flask, render_template

app=Flask(__name__)

@app.route("/salary")
def homepage1():
    name1= "babs"
    Salary1=2000
    return  render_template("salaryslip.html", name=name1, salary=Salary1)

app.run()