#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    var = list(storage.all(State).values())
    return render_template("8-cities_by_states.html", var=var)


@app.teardown_appcontext
def closer(err):
    """ close app context """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
