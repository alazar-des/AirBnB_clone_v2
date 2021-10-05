#!/usr/bin/python3
"""Start a web application.
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """return hello hbnb.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return hbnb.
    """
    return "HBNB"


@app.route('/c/<ctext>')
def cisfun(ctext):
    """Return input string.
    """
    return 'C %s' % ctext.replace("_", " ")


@app.route('/python')
@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """Return url.
    """
    return 'Python %s' % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
