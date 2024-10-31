#!/usr/bin/python3
"""
A Flask web application that displays 'Hello HBNB!' at the root route.

Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the root route."""
    return "Hello HBNB!"

if __name__ == "__main__":
    # Runs the application on host 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
