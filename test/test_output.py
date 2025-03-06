import pytest
from unittest.mock import patch
from app import create_app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app(testing=True)
    return app.test_client()

@patch("app.views.render_template", return_value="Mocked HTML Response")
@patch("app.models.predict_risk")
def test_output_success(mock_predict_risk, mock_render_template, client):
    """Test the /output route with a valid form submission."""
    mock_predict_risk.return_value = 1  

    data = {
        "Age": "55",
        "Sex": "1",
        "ChestPainType": "2",
        "Cholesterol": "200",
        "FastingBS": "0",
        "MaxHR": "160",
        "ExerciseAngina": "0",
        "Oldpeak": "1.2",
        "ST_Slope": "2",
    }

    response = client.post("/output", data=data)

    assert response.status_code == 200
    assert b"Mocked HTML Response" in response.data  

@patch("app.views.render_template", return_value="Mocked Error Response")
@patch("app.models.predict_risk")
def test_output_missing_values(mock_predict_risk, mock_render_template, client):
    """Test /output route with missing form values."""
    mock_predict_risk.return_value = 1

    data = {
        "Age": "55",
        "Sex": "1",
        # Missing ChestPainType
        "Cholesterol": "200",
        "FastingBS": "0",
        "MaxHR": "160",
        "ExerciseAngina": "0",
        "Oldpeak": "1.2",
        "ST_Slope": "2",
    }

    response = client.post("/output", data=data)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Missing value for ChestPainType parameter"}

@patch("app.views.render_template", return_value="Mocked HTML Response")
@patch("app.models.predict_risk")
def test_output_json_response(mock_predict_risk, mock_render_template, client):
    """Test the /output route with form-encoded data."""
    mock_predict_risk.return_value = 0  

    data = {
        "Age": "45",
        "Sex": "0",
        "ChestPainType": "1",
        "Cholesterol": "180",
        "FastingBS": "1",
        "MaxHR": "150",
        "ExerciseAngina": "1",
        "Oldpeak": "0.8",
        "ST_Slope": "1",
    }

    response = client.post("/output", data=data)  
    assert response.status_code == 200
    assert b"Mocked HTML Response" in response.data 
