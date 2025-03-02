# Corrected model path in models.py
import pickle
import os


print("Current Directory:", os.getcwd())
# Load the pre-trained model (ensure the path is correct)


model_path: str = "./models/model_and_data.pkl"
with open(model_path, "rb") as file:
    loaded_model, loaded_data = pickle.load(file)


def predict_risk(features: list[int | float | str]) -> int:
    """Predict the risk based on the input parameters.
    Args:
        features (list[int]): The input features for the model
    Returns:
        int: The predicted risk value
    """
    # Prepare data for the model if needed
    print(loaded_data.head())
    print(features)
    # Make prediction
    # prediction: list[int] = loaded_model.predict([features])
    # Return the prediction result
    # return prediction[0]
    return 0
