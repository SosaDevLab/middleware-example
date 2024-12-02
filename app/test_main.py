from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_authorized_access():
    """
    Test the authorized access to the root endpoint.

    This test sends a GET request to the root endpoint with an "X-User" header
    set to "SosaDevLab" and checks if the response status code is 200. It also
    verifies that the JSON response contains the expected message.

    Assertions:
        - The response status code should be 200.
        - The JSON response should contain the expected message indicating
          that the password is not included.
    """
    response = client.get("/", headers={"X-User": "SosaDevLab"})
    assert response.status_code == 200
    assert response.json() == {
        "contraseña": "Enserio pensaron que iba a poner la contraseña aquí?"}


def test_unauthorized_access():
    """
    Test unauthorized access to the root endpoint.

    This test sends a GET request to the root endpoint with an unauthorized user header.
    It asserts that the response status code is 401 (Unauthorized) and the response JSON
    contains the expected error message.

    Assertions:
        - The response status code should be 401.
        - The response JSON should be {"error": "Bro???"}.
    """
    response = client.get("/", headers={"X-User": "SosaDevLabn't"})
    assert response.status_code == 401
    assert response.json() == {"error": "Bro???"}


def test_no_headers_request():
    """
    Test case for making a GET request to the root endpoint without headers.

    This test ensures that when a request is made to the root endpoint ("/")
    without any headers, the response status code is 401 (Unauthorized) and
    the response body contains the expected error message.

    Assertions:
        - The response status code should be 401.
        - The response JSON should be {"error": "Bro???"}.
    """
    response = client.get("/")
    assert response.status_code == 401
    assert response.json() == {"error": "Bro???"}
