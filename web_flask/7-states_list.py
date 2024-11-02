#!/usr/bin/python3
""" Flask web application to display states list """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the list of states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    # Log message to confirm the app is running
    print("Starting Flask app on http://0.0.0.0:5000")
    
    try:
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        print(f"Error starting Flask server: {e}")
