#!/usr/bin/python3

"""Set up API with flask."""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down():
    """Close active session."""
    storage.close()


if __name__ == "__main__":
    port = getenv('HBNB_API_PORT', default=5000)
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    app.run(host, int(port), threaded=True)
