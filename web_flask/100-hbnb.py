#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def states():
    stat = list(storage.all(State).values())
    ameni = list(storage.all(Amenity).values())
    plac = list(storage.all(Place).values())
    usr = list(storage.all(User).values())
    return render_template("100-hbnb.html", stat=stat, ameni=ameni,
                           plac=plac, usr=usr)


@app.teardown_appcontext
def closer(err):
    """ close app context """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
