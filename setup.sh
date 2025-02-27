#!/bin/bash

echo "Setting up the Python virtual environment and installing dependencies..."

# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install required Python packages from requirements.txt
pip install -r requirements.txt

echo "Environment setup complete. You can now run the Flask app locally."

# Optional: commands to start the Flask app or other services can be added here
# flask run --host=0.0.0.0 --port=5000
