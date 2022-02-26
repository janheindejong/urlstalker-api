"""SQLAlchemy models"""

from __future__ import annotations

from typing import Any

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base: Any = declarative_base()


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True)
    path = Column(String)
    snapshots: list[SnapShot] = relationship("SnapShot", cascade="all, delete-orphan")


class SnapShot(Base):
    __tablename__ = "snapshots"

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    status_code = Column(Integer)
    response = Column(String)
    resource_id = Column(Integer, ForeignKey("resources.id"))
