#!/usr/bin/python3
"""A script that starts a Flask application listening on 0.0.0.0, port 5000
Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display "n is a number" only if n is an integer
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns a given string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns a given string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display 'C' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """displays 'python' followed by the value of the text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
