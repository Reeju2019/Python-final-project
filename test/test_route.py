import sys
import os

# Get the absolute path of the project root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app  # Now Python can find the `app` module
from flask_testing import TestCase


class TestRoutes(TestCase):
    def create_app(self):
        return create_app()

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Heart Disease Risk Prediction", response.data.decode())
