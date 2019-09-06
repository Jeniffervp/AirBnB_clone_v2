#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask


hbnb = Flask(__name__)
hbnb.url_map.strict_slashes = False


@hbnb.route('/')
def hi_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
