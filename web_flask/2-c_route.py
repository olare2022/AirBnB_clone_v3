#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
        """Displays 'Hello HBNB!'."""
            return "Hello HBNB!"


            @app.route("/hbnb", strict_slashes=False)
            def hbnb():
                    """Displays 'HBNB'."""
                        return "HBNB"


                        @app.route("/c/<text>", strict_slashes=False)
                        def c(text):
                                """Displays 'C' followed by the value of <text>."""
                                    text = text.replace("_", " ")
                                        return "C {}".format(text)


                                        if __name__ == "__main__":
                                                app.run(host="0.0.0.0")
=======
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
