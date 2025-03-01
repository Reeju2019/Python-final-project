#!/bin/bash

echo "Setting up the Python virtual environment and installing dependencies..."

# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install required Python packages from requirements.txt
cd ..
pip install -r requirements.txt

echo "Environment setup complete. You can now run the Flask app locally."

# Start the Flask app
python app.py
