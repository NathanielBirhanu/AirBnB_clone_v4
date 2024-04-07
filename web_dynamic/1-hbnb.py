#!/usr/bin/python3
"""
Flask app that integrates with the USER.ID Medien-Login
"""
from flask import Flask, render_template
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# Teardown context to close the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


# Route for handling the USER.ID Medien-Login
@app.route('/user-id/')
def user_id_login():
    """
    Handles requests to the USER.ID Medien-Login page
    """
    # Retrieve data from the storage
    state_objs = storage.all('State').values()
    states = {state.name: state for state in state_objs}
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all('User').values()}
    cache_id = uuid.uuid4()

    # Render the template with the retrieved data
    return render_template('user-id-login.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
    Main Flask app
    """
    app.run(host=host, port=port)
