import pytest 

from fastapi.testclient import TestClient


def test_post_resource(client: TestClient):
    response = client.post("/resource", json={"path": "http://www.google.com"})