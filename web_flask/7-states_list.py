#!/usr/bin/python3
"""this module starts a flask web application"""
from models import storage, State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def cities_by_states():
    """fetches the storage engine and renders html template"""
    return render_template("7-states_list.html", states=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """remove the current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
