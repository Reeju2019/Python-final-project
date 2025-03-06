import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app

# from model import model
import unittest


class TestModelIntegration(unittest.TestCase):
    def test_prediction(self):
        app = create_app()
        # with app.app_context():
        #     prediction = model.predict([])  # replace 'input_data' with actual data
        #     self.assertIsNotNone(prediction)  # or other assertions based on your model's output
