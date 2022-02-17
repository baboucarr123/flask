from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
    return """
    <html>
    <h1> <u> Welcome to my homepage </U> </hl>
    <br>
    we are the only building society in the UK
    <br>
    <br>
    <a href="http://localhost:5000/services"> Our Services </a> <br>
    <a href="http://localhost:5000/Team"> who we are </a> <br>
    </html>
    """

@app.route("/Team")
def message ():
      return """
    <html>
    <h1> <u> This is the team </u> </hl>
    <br>
    <a href="http://localhost:5000">Home </a>
     <ul>
    <li> Baboucarr -Director</li>
    <li> Shafeeq- lecture</li>
    <li> Hayley - HR</li>
    </ul>
    </html>
    """

@app.route("/services")
def boom ():
    return """
    <html>
    <h2> we prodive the following services</h2>
    <br>
    <a href="http://localhost:5000">Home </a>
    <br>
    <ul>
    <li> Open Account</li>
    <li> deposit</li>
    <li> withdraw</li>
    </ul>
    </html>
    
    """

app.run()