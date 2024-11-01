#!/usr/bin/python3
from flask import Flask  # Import the Flask class from the flask module

# Create a Flask instance
app = Flask(__name__)

# Define a route for the root URL "/"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a welcome message at the root URL (/)"""
    return "Hello HBNB!"

# Define a route for "/hbnb"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a message specific to the /hbnb URL"""
    return "HBNB"

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Listen on all IP addresses at port 5000
