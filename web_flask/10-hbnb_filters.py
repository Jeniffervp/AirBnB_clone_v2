#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def states():
    var = list(storage.all(State).values())
    var2 = list(storage.all(Amenity).values())
    return render_template("10-hbnb_filters.html", var=var, var2=var2)


@app.teardown_appcontext
def closer(err):
    """ close app context """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
