#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    my_dict = storage.all(State)
    var = list(my_dict.values())
    find_id = None

    if id is not None:
        k = "State.{}".format(id)
        if k in my_dict:
            find_id = 1
            var = [my_dict[k]]
    return render_template("9-states.html", var=var,
                           find_id=find_id, id=id)


@app.teardown_appcontext
def closer(err):
    """ close app context """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
