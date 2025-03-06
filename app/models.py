import pickle
import numpy as np


def load_preprocessors():
    with open("./models/preprocessors.pkl", "rb") as f:
        le, mms, ss = pickle.load(f)
    return le, mms, ss


def load_model():
    with open("./models/model_and_data.pkl", "rb") as model_file:
        model, data = pickle.load(model_file)
    return model


def preprocess_input_data(input_data, le, mms, ss):
    # Label encode categorical variables (same as done during training)
    try:
        input_data[1] = le.transform([input_data[1]])[0]  # Sex
    except ValueError:
        print(f"Unseen label encountered for 'Sex': {input_data[1]}")
        input_data[1] = 0  # Set a default value (e.g., 0 for Male)

    try:
        input_data[2] = le.transform([input_data[2]])[0]  # ChestPainType
    except ValueError:
        print(f"Unseen label encountered for 'ChestPainType': {input_data[2]}")
        input_data[2] = 0  # Set a default value

    try:
        input_data[6] = le.transform([input_data[6]])[0]  # ExerciseAngina
    except ValueError:
        print(f"Unseen label encountered for 'ExerciseAngina': {input_data[6]}")
        input_data[6] = 0  # Set a default value

    try:
        input_data[8] = le.transform([input_data[8]])[0]  # ST_Slope
    except ValueError:
        print(f"Unseen label encountered for 'ST_Slope': {input_data[8]}")
        input_data[8] = 0  # Set a default value

    # Handle 'FastingBS' and 'MaxHR' as categorical if they have non-numeric values like 'Y'/'N'
    if isinstance(input_data[4], str):  # Check if 'FastingBS' is categorical
        try:
            input_data[4] = le.transform([input_data[4]])[0]  # FastingBS
        except ValueError:
            print(f"Unseen label encountered for 'FastingBS': {input_data[4]}")
            input_data[4] = 0  # Set a default value

    if isinstance(input_data[5], str):  # Check if 'MaxHR' is categorical
        try:
            input_data[5] = le.transform([input_data[5]])[0]  # MaxHR
        except ValueError:
            print(f"Unseen label encountered for 'MaxHR': {input_data[5]}")
            input_data[5] = 0  # Set a default value

    # Normalize 'Oldpeak'
    input_data[7] = mms.transform(np.array(input_data[7]).reshape(-1, 1))[0][
        0
    ]  # Oldpeak

    # Standardize numerical features
    input_data[0] = ss.transform(np.array(input_data[0]).reshape(-1, 1))[0][0]  # Age
    input_data[3] = ss.transform(np.array(input_data[3]).reshape(-1, 1))[0][
        0
    ]  # Cholesterol
    input_data[4] = ss.transform(np.array(input_data[4]).reshape(-1, 1))[0][
        0
    ]  # FastingBS
    input_data[5] = ss.transform(np.array(input_data[5]).reshape(-1, 1))[0][0]  # MaxHR

    return np.array(input_data).reshape(1, -1)  # Reshape for model input


def predict_risk(input_data):
    model = load_model()
    le, mms, ss = load_preprocessors()

    processed_input = preprocess_input_data(input_data, le, mms, ss)
    if processed_input is None:
        return "Prediction cannot be made due to input processing error."

    prediction = model.predict(processed_input)
    return prediction[0]
