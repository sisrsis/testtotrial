from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "holoword"




@app.route("/testurl")
def test():
    return "test project git "
@app.route("/te")
def testtt():
    return "test hllo world"