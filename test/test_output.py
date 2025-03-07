import pytest
from unittest.mock import patch, MagicMock
from app import create_app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app(testing=True)
    return app.test_client()

@patch("app.models.load_model")
@patch("app.models.load_preprocessors")
@patch("app.views.render_template", return_value="Mocked HTML Response")
@patch("app.models.predict_risk")
def test_output_success(mock_predict_risk, mock_render_template, mock_load_preprocessors, mock_load_model, client):
    """Test the /output route with a valid form submission."""

    # Create mock preprocessors
    mock_le = MagicMock()
    mock_mms = MagicMock()
    mock_ss = MagicMock()

    # Set up mock transform behavior for LabelEncoder and other preprocessors
    mock_le.transform.side_effect = lambda x: [x[0]]  # Simple identity transform for testing
    mock_mms.transform.side_effect = lambda x: x  # Identity transform for MinMaxScaler
    mock_ss.transform.side_effect = lambda x: x  # Identity transform for StandardScaler

    # Create a mock model with a mock 'predict' method
    mock_model = MagicMock()
    mock_model.predict.return_value = [1]  # Simulating a prediction output

    # Mocking the model and preprocessor loading
    mock_load_model.return_value = mock_model  # Return the mocked model
    mock_load_preprocessors.return_value = (mock_le, mock_mms, mock_ss)  # Return mocked preprocessors

    # Mock the prediction output (this is redundant now but kept for clarity)
    mock_predict_risk.return_value = 1  

    # Input data for testing
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

@patch("app.models.load_model")
@patch("app.models.load_preprocessors")
@patch("app.views.render_template", return_value="Mocked Error Response")
@patch("app.models.predict_risk")
def test_output_missing_values(mock_predict_risk, mock_render_template, mock_load_preprocessors, mock_load_model, client):
    """Test /output route with missing form values."""

    # Create mock preprocessors
    mock_le = MagicMock()
    mock_mms = MagicMock()
    mock_ss = MagicMock()

    # Set up mock transform behavior for LabelEncoder and other preprocessors
    mock_le.transform.side_effect = lambda x: [x[0]]  # Simple identity transform for testing
    mock_mms.transform.side_effect = lambda x: x  # Identity transform for MinMaxScaler
    mock_ss.transform.side_effect = lambda x: x  # Identity transform for StandardScaler

    # Create a mock model with a mock 'predict' method
    mock_model = MagicMock()
    mock_model.predict.return_value = [1]  # Simulating a prediction output

    # Mocking the model and preprocessor loading
    mock_load_model.return_value = mock_model  # Return the mocked model
    mock_load_preprocessors.return_value = (mock_le, mock_mms, mock_ss)  # Return mocked preprocessors

    # Mock the prediction output (this is redundant now but kept for clarity)
    mock_predict_risk.return_value = 1  

    # Input data with missing "ChestPainType"
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

@patch("app.models.load_model")
@patch("app.models.load_preprocessors")
@patch("app.views.render_template", return_value="Mocked HTML Response")
@patch("app.models.predict_risk")
def test_output_json_response(mock_predict_risk, mock_render_template, mock_load_preprocessors, mock_load_model, client):
    """Test the /output route with form-encoded data."""

    # Create mock preprocessors
    mock_le = MagicMock()
    mock_mms = MagicMock()
    mock_ss = MagicMock()

    # Set up mock transform behavior for LabelEncoder and other preprocessors
    mock_le.transform.side_effect = lambda x: [x[0]]  # Simple identity transform for testing
    mock_mms.transform.side_effect = lambda x: x  # Identity transform for MinMaxScaler
    mock_ss.transform.side_effect = lambda x: x  # Identity transform for StandardScaler

    # Create a mock model with a mock 'predict' method
    mock_model = MagicMock()
    mock_model.predict.return_value = [0]  # Simulating a prediction output

    # Mocking the model and preprocessor loading
    mock_load_model.return_value = mock_model  # Return the mocked model
    mock_load_preprocessors.return_value = (mock_le, mock_mms, mock_ss)  # Return mocked preprocessors

    # Mock the prediction output (this is redundant now but kept for clarity)
    mock_predict_risk.return_value = 0  

    # Input data for testing
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
