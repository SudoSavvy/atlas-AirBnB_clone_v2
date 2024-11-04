#!/usr/bin/python3
"""Flask web application to display States and Cities"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """Displays a page with a list of all State objects in storage"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays a page for a specific State with its Cities"""
    state = None
    states = storage.all(State)
    for st in states.values():
        if st.id == id:
            state = st
            break
    return render_template('9-states.html', state=state)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
