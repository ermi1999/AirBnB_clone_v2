#!/usr/bin/python3
"""this module starts a flask web application"""
from models import storage, State, Amenity, City
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """fetches the storage engine and renders html template"""
    return render_template("10-hbnb_filters.html",
                           states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def teardown(exc):
    """remove the current sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)