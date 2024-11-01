#!/usr/bin/python3
"""
Module: 7-states_list
Description: Starts a Flask web application to display a list of all State
             objects from a database, sorted by name.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects."""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)  # Sort states by name
    return render_template('7-states_list.html', states=sorted_states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
