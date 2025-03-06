# Heart Disease Prediction Web App

## Overview

This Flask web application predicts the risk of heart disease based on user inputs about their symptoms and lifestyle. It utilizes a machine learning model trained on a comprehensive dataset to provide predictions. The application is designed to be user-friendly and responsive, accessible via web browsers on various devices.

The live application can be accessed at [Heart Disease Prediction App](https://myflaskapp-latest.onrender.com).

## Dataset

The machine learning model was trained using a dataset focused on heart disease risk factors, which can be explored on Kaggle: [Heart Failure Prediction](https://www.kaggle.com/code/tanmay111999/heart-failure-prediction-cv-score-90-5-models/input).

## Features

-   **Predictive Modeling**: Utilizes a trained model to predict heart disease risk.
-   **User Interface**: Simple and intuitive form for inputting symptoms and risk factors.
-   **Accessibility**: Fully accessible via web browsers on desktops and mobile devices.

## Installation

### Prerequisites

-   Docker
-   Git (optional, recommended for version control)

### Local Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Reeju2019/Python-final-project
    cd Python-final-project
    ```

2. **Build the Docker container:**

    ```bash
    docker build -t myflaskapp .
    ```

3. **Run the container:**

    ```bash
    docker run -p 5000:5000 myflaskapp
    ```

    Access the application at [http://localhost:5000](http://localhost:5000).

### Using the Live Application

Simply visit [Heart Disease Prediction App](https://myflaskapp-latest.onrender.com) to use the application deployed on Render.

## Usage

To use the application, follow these steps:

1. Navigate to the URL provided.
2. Fill in the details in the form regarding symptoms and lifestyle factors.
3. Submit the form to receive the risk prediction of heart disease.

## Contributing

Contributions to the project are welcome! Please consider the following steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Code Documentation

For code documentation we have used Sphinx. To run the document

1. Go to the doc folder.
2. Then Build folder
3. Then run the index.html file in your local browser
4. After updating the code please update the sphinx doc as well.
5. to update the doc run the command 'sphinx-build -b html docs/source docs/build'in the doc folder.

## Acknowledgements

-   Dataset provided by [Kaggle - Heart Failure Prediction](https://www.kaggle.com/code/tanmay111999/heart-failure-prediction-cv-score-90-5-models/input).
-   Hosting provided by [Render](https://render.com).

## License

This project is licensed under the [MIT License](https://github.com/Reeju2019/Python-final-project/blob/master/LICENSE).
