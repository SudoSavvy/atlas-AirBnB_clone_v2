#!/usr/bin/python3
"""
A Flask web application that displays a list of states from a database.
The application listens on 0.0.0.0, port 5000, and uses DBStorage for data retrieval.

Routes:
    /states_list: Displays a list of states in HTML format.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders an HTML page with a list of all State objects."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
