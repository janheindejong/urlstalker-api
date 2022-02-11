import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from urlstalker.app import app, get_db
from urlstalker.models import Base

from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.pool import StaticPool

from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine("sqlite://", connect_args={'check_same_thread': False}, echo=True, poolclass=StaticPool)
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    # bind an individual Session to the connection
    db = Session(bind=db_engine)
    db.begin()
    yield db
    db.rollback()
    db.close()


@pytest.fixture(scope="function")
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c
