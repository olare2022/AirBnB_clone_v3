#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
