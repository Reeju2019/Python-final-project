Usage
=====

The **Heart Disease Prediction** application is a web-based app built using Flask. 

1. **Enter patient details** on the homepage (like age, sex, cholesterol level, etc.).
2. **Submit the form** to get a prediction on whether the patient is at risk of heart disease.

To interact with the backend, the app uses the following route:
POST /predict
This route receives data via a form submission, makes predictions using the pre-trained 
machine learning model, and returns the result.
