# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance
ip = "this is the ip address 1.1.1.1"

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "" + ip         # which returns "hello world"s


if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
