#!/usr/bin/python3

"""Index file for 'views' dir."""

from api.views import app_views


@app_views.route('/status', strict_slashes=False)
def check_status():
    """Return JSON status."""
    return jsonify({"status": "OK"})
