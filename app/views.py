from typing import Union
from flask import Blueprint, render_template, request, jsonify

from app.models import predict_risk

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home() -> str:
    """Render the homepage.
    Args:
        None
    Returns:
        str: The rendered HTML content
    """
    return render_template("home.html")


@views.route("/predict", methods=["GET"])
def predict() -> str:
    """Render input form.
    Args:
        None
    Returns:
        str: The rendered HTML content
    """
    return render_template("index.html")


@views.route("/about", methods=["GET"])
def about() -> str:
    """Render the About Us page.
    Args:
        None
    Returns:
        str: The rendered HTML content
    """
    return render_template("about.html")


@views.route("/output", methods=["POST"])
def output() -> Union[str, tuple]:
    """Receive data from the form, use the model to make predictions, and show results.
    Args:
        None
    Returns:
        Union[str, tuple]: The rendered HTML content or a JSON response with status code
    """
    # Define feature keys to extract data more dynamically and ensure consistency
    # feature_keys: list[str] = [
    #     "age",
    #     "chest_pain",
    #     "shortness_of_breath",
    #     "fatigue",
    #     "palpitations",
    #     "dizziness",
    #     "swelling",
    #     "radiating_pain",
    #     "cold_sweats",
    #     "blood_pressure",
    #     "cholesterol_high",
    #     "diabetes",
    #     "smoker",
    #     "obesity",
    #     "family_history",
    # ]
    feature_keys: list[str] = [
        "Age",
        "Sex",
        "ChestPainType",
        "Cholesterol",
        "FastingBS",
        "MaxHR",
        "ExerciseAngina",
        "Oldpeak",
        "ST_Slope",
    ]

    # Extract data from form and convert parameters to int or float or string
    features: list[int | float | str] = []
    for key in feature_keys:
        value = request.form.get(key)
        if value is None:
            return (
                jsonify({"error": f"Missing value for {key} parameter"}),
                400,
            )
        try:
            features.append(int(value))
        except ValueError:
            try:
                features.append(float(value))
            except ValueError:
                features.append(str(value))

    # Call the model prediction function, assuming it accepts a list of ints
    result: int = predict_risk(
        features
    )  # Ensure this function is imported and defined properly

    # Render the output page with the prediction result
    return render_template(
        "output.html", prediction_result=True if result == 1 else False
    )
