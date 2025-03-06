import pytest
import sys
import os

# Ensure the app module is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app  # ✅ Import `create_app()` from `app/__init__.py`

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config["TESTING"] = True
    return app

@pytest.fixture
def client(app):
    """Flask test client fixture."""
    return app.test_client()

