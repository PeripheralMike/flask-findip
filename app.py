# app.py
from flask import Flask           # import flask
import ipgetter2
from ipgetter2 import ipgetter1 as ipgetter
myip = ipgetter.myip()

app = Flask(__name__)
@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "" + myip      # which returns "hello world"s

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
