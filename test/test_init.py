import sys
import os
import unittest
from app import create_app

# Ensure the project root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class TestInit(unittest.TestCase):
    """ Tests for the create_app function in __init__.py """

    def setUp(self):
        """ Runs before each test case. Initializes the Flask app. """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_app_creation(self):
        """ The Flask application should be successfully created """
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.name, "app")

    def test_app_config(self):
        """ Check if the application is in test mode """
        self.assertFalse(self.app.testing)  # Change to True if needed

    def test_blueprint_registration(self):
        """ Ensure that blueprints are correctly registered """
        registered_prefixes = [bp.url_prefix or "/" for bp in self.app.blueprints.values()]
        self.assertIn("/", registered_prefixes)

    def test_home_route(self):
        """ The home route ("/") should be accessible """
        response = self.client.get("/")
        self.assertIn(response.status_code, [200, 302])  # 200: OK, 302: Redirect

if __name__ == "__main__":
    unittest.main()
