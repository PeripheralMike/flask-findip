# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance
import urllib.request
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "" + external_ip         # which returns "hello world"s


if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
