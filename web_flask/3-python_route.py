#!/usr/bin/python3
"""
A Flask web application with multiple routes.

Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C " followed by the value of the `text` variable,
               with underscores (_) replaced by spaces.
    /python/(<text>): Displays "Python " followed by the value of the `text`
                      variable, with underscores (_) replaced by spaces.
                      If no `text` is provided, defaults to "is cool".

The application listens on 0.0.0.0 and runs on port 5000.
All routes use strict_slashes=False to allow URLs with or without a trailing slash.
"""

from flask import Flask  # Import Flask to create a web application instance

# Initialize a new Flask web application instance
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Root URL route handler.

    Returns:
        str: A welcome message "Hello HBNB!" displayed at the root URL (/).
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    /hbnb route handler.

    Returns:
        str: The message "HBNB" displayed at the /hbnb URL.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    /c/<text> route handler.

    Args:
        text (str): A variable part of the URL to display after "C ".
                    Underscores (_) in the text are replaced with spaces.

    Returns:
        str: A string starting with "C " followed by the value of the `text` variable.
    """
    # Replace underscores with spaces in the `text` variable
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    /python/(<text>) route handler.

    Args:
        text (str, optional): A variable part of the URL to display after "Python ".
                              Underscores (_) in the text are replaced with spaces.
                              Defaults to "is cool" if no value is provided.

    Returns:
        str: A string starting with "Python " followed by the value of the `text` variable.
    """
    # Replace underscores with spaces in the `text` variable
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"

if __name__ == "__main__":
    # Run the Flask application, listening on all available IP addresses (0.0.0.0) and port 5000.
    app.run(host="0.0.0.0", port=5000)
