#!/usr/bin/python3
"""Start a web application.
"""
from flask import Flask, render_template


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
def python(text='cool'):
    """Return url.
    """
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """Return if int.
    """
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """Return html template.
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Return html template.
    """
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run()
