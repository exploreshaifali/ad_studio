from fastapi.testclient import TestClient

from ad_studio import __version__

from ad_studio.main import app


client = TestClient(app)


def test_version():
    assert __version__ == '0.1.0'


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}
