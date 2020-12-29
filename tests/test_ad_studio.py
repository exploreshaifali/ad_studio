import os

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


def test_process_feed():
	csv_data = open(os.path.dirname(__file__)+"/test_data/data_feed.csv", "rb")
	response = client.post("/feed/?template_id=3", files={"file": csv_data, "content_type": "multipart/form-data"})
	assert response.status_code == 201
	assert response.json() == {"message": "Images Generated"}
