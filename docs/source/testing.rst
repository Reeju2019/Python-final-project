Testing
=======

This section documents the tests for the **Heart Disease Prediction** app. The tests are written 
using the `unittest` framework and ensure the correctness of the backend functionality.

### Unit Tests
Unit tests are located in the `test` folder. They include tests for:
- **Route Testing**: Ensuring that all routes (like `/predict`) return the correct responses.
- **Model Testing**: Ensuring that the prediction model produces expected results with sample data.

Example of testing a route:

```python
def test_homepage(client):
    """Test if homepage loads successfully."""
    response = client.get('/')
    self.assertEqual(response.status_code, 200)