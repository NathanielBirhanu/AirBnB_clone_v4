#!/usr/bin/python3
"""
Flask App that integrates with XYZ static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import random


# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# Teardown database after each request
@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e., .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


# Custom route for rendering XYZ template
@app.route('/xyz/')
def xyz_filters():
    """
    Handles requests to custom template with various filters
    """
    categories = ['Category A', 'Category B', 'Category C']
    items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    users = {
        'user1': 'John Doe',
        'user2': 'Jane Smith',
        'user3': 'Robert Johnson'
    }
    random_number = random.randint(1, 100)
    return render_template('xyz.html',
                           categories=categories,
                           items=items,
                           users=users,
                           random_number=random_number)


if __name__ == "__main__":
    """
    Main Flask App
    """
    app.run(host=host, port=port)
