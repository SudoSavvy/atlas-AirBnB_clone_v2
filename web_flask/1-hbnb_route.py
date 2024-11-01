#!/usr/bin/python3
"""
A simple Flask web application with two routes:

Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"

The application listens on 0.0.0.0 and runs on port 5000.
It uses strict_slashes=False to allow URLs with or without a trailing slash.
"""

from flask import Flask  # Import the Flask class to create a web application instance

# Initialize a new Flask web application instance
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Root URL route handler.

    Returns:
        str: A welcome message "Hello HBNB!" to be displayed at the root URL (/).
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    /hbnb route handler.

    Returns:
        str: The message "HBNB" to be displayed at the /hbnb URL.
    """
    return "HBNB"

if __name__ == "__main__":
    # Run the Flask application, listening on all available IP addresses (0.0.0.0) and port 5000.
    app.run(host="0.0.0.0", port=5000)
