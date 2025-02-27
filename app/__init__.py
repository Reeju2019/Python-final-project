# app/__init__.py

from flask import Flask
from .views import views


def create_app() -> object:
    """Create and configure an instance of the Flask application.
    Args:
        None
    Returns:
        object: The Flask app instance
    """
    app: object = Flask(__name__)

    # You might want to configure a secret key for sessions, database URLs, etc.
    # app.config["SECRET_KEY"] = "your_secret_key"

    app.register_blueprint(views, url_prefix="/")

    return app
