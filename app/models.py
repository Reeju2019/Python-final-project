import pickle
import os
import pandas as pd

print("Current Directory:", os.getcwd())

# Load the pre-trained model (ensure the path is correct)
model_path: str = "./models/model_and_data.pkl"
with open(model_path, "rb") as file:
    loaded_model, loaded_data = pickle.load(file)

def predict_risk(features: list[int | float | str]) -> int:
    """Predict the risk based on the input parameters."""
    loaded_data = pd.DataFrame([features], columns=[
        "Age", "Sex", "ChestPainType", "Cholesterol", "FastingBS",
        "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"
    ])

    # Dummy prediction logic (replace this with your actual model prediction)
    # prediction = loaded_model.predict(loaded_data)
    prediction = 1 if loaded_data["Age"].values[0] > 50 else 0

    return prediction
