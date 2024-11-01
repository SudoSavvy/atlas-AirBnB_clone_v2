#!/usr/bin/python3
"""
A Flask web application that displays a list of states from a database.
The application listens on 0.0.0.0, port 5000, and uses DBStorage for data retrieval.

Routes:
    /states_list: Displays a list of states in HTML format.
    /add_state: Handles adding a new state to the database.
"""

from flask import Flask, render_template, request, redirect, url_for
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False, methods=['GET', 'POST'])
def states_list():
    """Renders an HTML page with a list of all State objects."""
    if request.method == 'POST':
        new_state_name = request.form.get('state_name')
        if new_state_name:
            new_state = State(name=new_state_name)
            storage.new(new_state)
            storage.save()
            return redirect(url_for('states_list'))

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
