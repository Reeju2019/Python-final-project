import unittest
from app import create_app

class TestViews(unittest.TestCase):
    """Tests for the views in views.py"""

    def setUp(self):
        """Runs before each test case to initialize the Flask app."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_homepage(self):
        """Test if the homepage ("/") loads successfully."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Heart Disease Risk Prediction", response.data)  # Check for expected content

if __name__ == "__main__":
    unittest.main()
