import pytest
from app import create_app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app(testing=True)
    return app.test_client()

def test_home(client):
    """Test the home route."""
    response = client.get("/")
    assert response.status_code == 200

def test_predict_page(client):
    """Test the predict page."""
    response = client.get("/predict")
    assert response.status_code == 200

def test_about(client):
    """Test the about page."""
    response = client.get("/about")
    assert response.status_code == 200
