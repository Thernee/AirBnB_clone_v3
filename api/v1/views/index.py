#!/usr/bin/python3

"""Index file for 'views' dir."""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def check_status():
    """Return JSON status."""
    return jsonify({"status": "OK"})
