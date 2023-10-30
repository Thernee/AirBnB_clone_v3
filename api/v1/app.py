#!/usr/bin/python3

"""Set up API with flask."""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(err):
    """Close active session."""
    storage.close()


@app.errorhandler(404)
def handle_404(error):
    """Set custom 404 page."""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    port = getenv('HBNB_API_PORT', default=5000)
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    app.run(host, int(port), threaded=True)
