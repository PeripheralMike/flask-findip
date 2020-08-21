# app.py
from flask import Flask                     # imports flask
import ipgetter2                            # imports ipgetter2
from ipgetter2 import ipgetter1 as ipgetter # uses the functions of the original ipgetter
myip = ipgetter.myip()                      #sets the variable of 'myip' to the external ip address

app = Flask(__name__)                       # generated the flask app
@app.route("/")                             # at the end point /
def hello():                                # call method hello
    return "" + myip                        # which returns the external ip address

if __name__ == "__main__":                  # on running python app.py
    app.run(host='0.0.0.0', port=8080)                               # run the flask app (add debug=True to run() to enter debug mode)
