#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB"
    /c/<text>: Displays “C” followed by the value of the variable
               (replace underscore _ symbols with a space ).
    /python/<text>: Displays “Python”, followed by the value of the variable
               (replace underscore _ symbols with a space ).
               The default value of text is “is cool”.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<var_text>", strict_slashes=False)
def c(var_text):
    """Display 'C' followed by the variable var_text value."""
    var_text = var_text.replace("_", " ")
    return "C {}".format(var_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<var_text>", strict_slashes=False)
def python(var_text="is cool"):
    """Display 'Python' followed by the value of var_text."""
    var_text = var_text.replace("_", " ")
    return "Python {}".format(var_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
