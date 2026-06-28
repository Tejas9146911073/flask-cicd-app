import pytest
from app import app as flask_app
@pytest.fixture
def app():
    yield flask_app
@pytest.fixture
def client(app):
    return app.test_client()
def test_home_page(client):
    """Test that home page returns 200 OK and expected text."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, CI/CD World!" in response.data
