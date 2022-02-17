from flask import Flask, render_template

app=Flask(__name__)

@app.route("/salary/<name>/<salary>")
def homepage1(name1,salary1):
    return  render_template("salaryslip.html", name=name1, salary=salary1)

app.run()