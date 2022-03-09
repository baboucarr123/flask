from flask import Flask, render_template, request, redirect
import mysql.connector

app=Flask(__name__)
db=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            database="nbs3"
)
mycursor =db.cursor()
@app.route("/")
def homepage(): 
    mycursor.execute("select * from personal")
    records=mycursor.fetchall();
    return render_template("Homepage.html",data=records)

@app.route("/departments/<dept>")
def departmentlist(dept):
    mycursor.execute("select * from personal where department='"+dept+"'")
    records=mycursor.fetchall();
    return render_template("Homepage.html",data=records)

@app.route("/newrecord")
def mewrecord():
    return render_template("inputform.html")


@app.route("/departmentEmployeesList")
def departmentEmployeesList():
    return render_template("listofemployees.html")

@app.route("/listofemployees",methods=['post'])
def listofemployees():
    dept=request.form["dept"]
    if dept=="all":
        mycursor.execute("select * from personal")
    else:
        mycursor.execute("select * from personal where department='"+dept+"'")
    records=mycursor.fetchall();
    return render_template("Homepage.html",data=records)

@app.route("/enternewpayslip")
def enternewpayslip():
    return render_template("payslip.html")

@app.route("/newsalary", methods=["post"])
def newsalary():
    amount=request.form["amount"]
    empno=request.form["empno"]
    Sq11="insert into accounts(empno,SalaryDate,amount) values ({0}, now(),{1})".format(empno,amount)
    mycursor.execute(Sq11)
    db.commit()
    return redirect("/")

@app.route("/saverecord", methods=["post"])
def saverecord():
    name=request.form["na"]
    dept=request.form["dept"]
    Sq11="insert into personal(name,department) values('{0}','{1}')".format(name,dept)
    mycursor.execute(Sq11)
    db.commit()
    return redirect("/")

@app.route("/details/<empno>")
def detials(empno):
    mycursor.execute("select * from personal where empno='"+empno+"'")
    personalrecord=mycursor.fetchall();
    mycursor.execute("select * from accounts where empno='"+empno+"'")
    salaryrecords=mycursor.fetchall();
    return render_template("details.html",personal=personalrecord,accounts=salaryrecords)

app.run(debug=True)


