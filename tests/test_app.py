from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_get_resource(client: TestClient, mock_data: Any):
    response = client.get("/resource")
    assert response.json() == mock_data


def test_post_resource(client: TestClient, db: Session, mock_data: Any):
    response = client.post("/resource", json={"path": "http://www.google.com"})
    assert response.json() == {
        "path": "http://www.google.com",
        "id": 2,
        "snapshots": [],
    }
