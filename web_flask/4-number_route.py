#!/usr/bin/python3
"""
    script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route('/number/<n>', strict_slashes=False)
def is_a_integer(number):
    if isinstance(number, int):
        return f"{number} is a number"
    return


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
