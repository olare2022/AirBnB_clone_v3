#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
        """Displays an HTML page with a list of all State objects in DBStorage.
            States are sorted by name.
            """
            states = storage.all("State")
                return render_template("7-states_list.html", states=states)


                @app.teardown_appcontext
                def teardown(exc):
                        """Remove the current SQLAlchemy session."""
                            storage.close()


                            if __name__ == "__main__":
                                    app.run(host="0.0.0.0")
=======
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
