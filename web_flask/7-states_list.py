#!/usr/bin/python3
""" starts flask wep app module.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/states_list')
def state():
    """ load all states.
    """
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
