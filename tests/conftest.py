from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from urlstalker.app import app, get_db
from urlstalker.models import Base, Resource, SnapShot


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine: Engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)
    yield db
    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def mock_data(db: Session):
    resource = Resource(path="https://www.helloworld.com")
    resource.snapshots = [
        SnapShot(
            datetime=datetime(1987, 10, 22, 0, 0),
            status_code=200,
            response="Hello, world!",
        )
    ]
    db.add(resource)
    db.commit()
    return [
        {
            "path": "https://www.helloworld.com",
            "id": 1,
            "snapshots": [
                {
                    "datetime": "1987-10-22T00:00:00",
                    "status_code": 200,
                    "response": "Hello, world!",
                    "id": 1,
                }
            ],
        }
    ]


@pytest.fixture(scope="function")
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c
