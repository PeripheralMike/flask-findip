# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance
import requests

myip = requests.get('https://www.google.com').headers['X-Client-IP']

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "" + myip       # which returns "hello world"s

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
