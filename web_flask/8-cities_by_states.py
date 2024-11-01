#!/usr/bin/python3
"""
Flask web application that displays cities by states.
This module contains a Flask application that fetches and displays all states
and their associated cities from the database.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
#!/usr/bin/python3
"""
8-cities_by_states.py

This module starts a Flask web application that displays states
and their associated cities in an HTML format. The application 
provides a route '/cities_by_states' that renders a template 
listing all states with their respective cities. 

The data is retrieved from a MySQL database using SQLAlchemy,
with a `State` model containing a one-to-many relationship with a 
`City` model. The application handles database sessions and 
ensures proper closure of sessions after each request.

Routes:
    - /cities_by_states: Displays a list of states and their cities.

Functions:
    - teardown_db: Closes the SQLAlchemy session after each request.
    - cities_by_states: Retrieves all states from the database, 
      sorted by name, and renders them in an HTML template.

Usage:
    Before running the application, set the following environment variables:
    
    - HBNB_MYSQL_USER: MySQL username
    - HBNB_MYSQL_PWD: MySQL password
    - HBNB_MYSQL_HOST: MySQL server address (default is 'localhost')
    - HBNB_MYSQL_DB: Name of the MySQL database to connect to
    - HBNB_TYPE_STORAGE: Type of storage ('db' for SQLAlchemy)

    Example command to run the application:
    HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd 
    HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db 
    HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states

Note:
    Ensure that the database is properly set up with 
    `State` and `City` models before running this application. 
    The template used for rendering should be placed in the 
    'web_flask/templates' directory and named '8-cities_by_states.html'.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with states and their cities."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with the list of all States and their Cities."""
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
