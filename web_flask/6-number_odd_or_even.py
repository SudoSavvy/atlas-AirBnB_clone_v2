#!/usr/bin/python3
"""
A Flask web application with multiple routes, including a route with HTML rendering
to display whether a number is odd or even.

Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C " followed by the value of the `text` variable,
               with underscores (_) replaced by spaces.
    /python/(<text>): Displays "Python " followed by the value of the `text`
                      variable, with underscores (_) replaced by spaces.
                      If no `text` is provided, defaults to "is cool".
    /number/<n>: Displays "n is a number" only if `n` is an integer.
    /number_template/<n>: Displays an HTML page only if `n` is an integer.
    /number_odd_or_even/<n>: Displays an HTML page only if `n` is an integer,
                             indicating whether `n` is odd or even.

The application listens on 0.0.0.0 and runs on port 5000.
All routes use strict_slashes=False to allow URLs with or without a trailing slash.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Root URL route handler."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb route handler."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    /c/<text> route handler.
    Replaces underscores with spaces in `text`.

    Args:
        text (str): Text to display after "C ".

    Returns:
        str: "C " followed by the formatted `text`.
    """
    return f"C {text.replace('_', ' ')}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    /python/(<text>) route handler.
    Displays "Python " followed by `text`, with underscores replaced by spaces.

    Args:
        text (str): Text to display after "Python ". Defaults to "is cool".

    Returns:
        str: "Python " followed by the formatted `text`.
    """
    return f"Python {text.replace('_', ' ')}"

@app.route('/number/<int:n>', strict_slashes=False)
def number_is_integer(n):
    """
    /number/<n> route handler.
    Displays "n is a number" if `n` is an integer.

    Args:
        n (int): The integer to check.

    Returns:
        str: "n is a number" if `n` is an integer.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    /number_template/<n> route handler.
    Renders an HTML page displaying the integer `n`.

    Args:
        n (int): The integer to display in the HTML template.

    Returns:
        HTML: HTML page with "Number: n".
    """
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    /number_odd_or_even/<n> route handler.
    Renders an HTML page displaying whether `n` is odd or even.

    Args:
        n (int): The integer to check for odd/even.

    Returns:
        HTML: HTML page with "Number: n is even" or "Number: n is odd".
    """
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
