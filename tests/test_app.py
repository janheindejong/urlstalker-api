from typing import Any

import fastapi
import pytest
from fastapi.testclient import TestClient


def test_get_resource(client: TestClient, mock_data: Any):
    response = client.get("/resource")
    assert response.json() == mock_data


def test_post_resource(client: TestClient, mock_data: Any):
    response = client.post("/resource", json={"path": "http://www.google.com"})
    assert response.json() == {
        "path": "http://www.google.com",
        "id": 2,
        "snapshots": [],
    }


def test_post_snapshot(client: TestClient, mock_data: Any):
    snapshot = {
        "datetime": "1987-10-22T01:23:45",
        "status_code": 200,
        "response": "This is me!",
    }
    response = client.post("/resource/1/snapshot", json=snapshot)
    assert response.json() == {**snapshot, **{"id": 2}}


def test_post_snapshot_resource_not_found(client: TestClient):
    snapshot = {
        "datetime": "1987-10-22T01:23:45",
        "status_code": 200,
        "response": "This is me!",
    }
    response = client.post("/resource/1/snapshot", json=snapshot)
    assert response.status_code == 422
    assert response.json()["detail"] == "Resource 1 not found"
