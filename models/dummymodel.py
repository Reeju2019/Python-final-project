import pickle
import os

dummy_model = "This is a dummy model"
dummy_data = {"example": 123}

os.makedirs("models", exist_ok=True)
with open("models/model_and_data.pkl", "wb") as file:
    pickle.dump((dummy_model, dummy_data), file)
