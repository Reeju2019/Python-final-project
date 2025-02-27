from joblib import load

# Load the pre-trained model (ensure the path is correct)
model_path: str = (
    "../models/best_model.joblib"  # Ensure the model is saved with .joblib extension
)
model = load(model_path)  # Load the model using joblib


def predict_risk(features: list[int]) -> int:
    """Predict the risk based on the input parameters.
    Args:
        features (list[int]): The input features for the model
    Returns:
        int: The predicted risk value

    """
    # Prepare data for the model if needed

    # Make prediction
    prediction: list[int] = model.predict([features])

    # Return the prediction result
    return prediction[0]
