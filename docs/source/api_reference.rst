===========================
API Reference Documentation
===========================

This document provides an overview of the available API endpoints in the application.

Home Route
-----------
**Endpoint:** `/`  
**Method:** `GET`  
**Description:**  
This route serves the homepage of the application. It renders the `home.html` template.

**Example Response:**

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to the Risk Prediction App</h1>
    </body>
    </html>

Prediction Input Route
----------------------
**Endpoint:** `/predict`  
**Method:** `GET`  
**Description:**  
This route serves the prediction input form where users can enter their health parameters for risk prediction.  
It renders the `index.html` template.

**Example Response:**

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Prediction</title>
    </head>
    <body>
        <h1>Enter your details for risk prediction</h1>
    </body>
    </html>

About Route
-----------
**Endpoint:** `/about`  
**Method:** `GET`  
**Description:**  
This route serves the About page of the application. It renders the `about.html` template, which provides information about the purpose of the application.

**Example Response:**

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>About</title>
    </head>
    <body>
        <h1>About the Risk Prediction App</h1>
    </body>
    </html>

Prediction Output Route
-----------------------
**Endpoint:** `/output`  
**Method:** `POST`  
**Description:**  
This route processes user input, passes it to the prediction model, and returns the risk assessment result.  
The response is either an HTML page (`output.html`) or a JSON object if requested via an API.

Request Parameters
^^^^^^^^^^^^^^^^^^
The request must contain the following form fields:

- **Age** (int)  
- **Sex** (str: `"M"` or `"F"`)  
- **ChestPainType** (str)  
- **Cholesterol** (int)  
- **FastingBS** (int)  
- **MaxHR** (int)  
- **ExerciseAngina** (str: `"0"` or `"1"`)  
- **Oldpeak** (float)  
- **ST_Slope** (str)  

If any of these parameters are missing, the API will return a `400 Bad Request` error with a JSON response:

.. code-block:: json

    {
        "error": "Missing value for <parameter> parameter"
    }

Example Request (Form Data Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: http

    POST /output HTTP/1.1
    Content-Type: application/x-www-form-urlencoded

    Age=55&Sex=M&ChestPainType=2&Cholesterol=200&FastingBS=0&MaxHR=160&ExerciseAngina=0&Oldpeak=1.2&ST_Slope=2

Example Request (JSON Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the request is sent as JSON, it should be formatted as follows:

.. code-block:: json

    {
        "Age": 55,
        "Sex": "M",
        "ChestPainType": "2",
        "Cholesterol": 200,
        "FastingBS": 0,
        "MaxHR": 160,
        "ExerciseAngina": "0",
        "Oldpeak": 1.2,
        "ST_Slope": "2"
    }

Example Response (JSON Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the request is sent as JSON, the response will also be in JSON format:

.. code-block:: json

    {
        "prediction": 1
    }

Example Response (HTML Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the request is sent via a form, the response will be an HTML page (`output.html`) displaying the prediction result:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Prediction Result</title>
    </head>
    <body>
        <h1>Prediction: Positive</h1>
    </body>
    </html>

Conclusion
----------
This API allows users to interact with the risk prediction model via a simple web interface and supports programmatic access via JSON responses.  
Ensure that all required fields are provided when submitting a request to the `/output` endpoint to avoid errors.
