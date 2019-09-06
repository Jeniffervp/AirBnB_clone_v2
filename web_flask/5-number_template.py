#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template


hbnb = Flask(__name__)
hbnb.url_map.strict_slashes = False


@hbnb.route('/')
def hi_hbnb():
    return "Hello HBNB!"


@hbnb.route('/hbnb')
def only_hbnb():
    return "HBNB"


@hbnb.route('/c/<text>')
def some_text(text):
    return "C {}".format(text.replace("_", " "))


@hbnb.route('/python')
@hbnb.route('/python/<text>')
def py_text(text="is_cool"):
        return "Python {}".format(text.replace("_", " "))


@hbnb.route('/number/<int:n>')
def some_number(n):
    return "{} is a number".format(n)


@hbnb.route('/number_template/<int:n>')
def num_template(n):
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
