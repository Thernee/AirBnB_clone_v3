#!/usr/bin/python3

"""Index file for 'views' dir."""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def check_status():
    """Return JSON status."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count_by_type():
    """Retrieve number of each object by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
