#!/usr/bin/python3
"""this module starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello hbnb when the root url is visited"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb when the url is /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
