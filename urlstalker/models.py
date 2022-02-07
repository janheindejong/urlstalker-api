"""SQLAlchemy models"""

from msilib.schema import Complus
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class EndPoint(Base):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True)
    path = Column(String)
    entries = relationship("Entry", cascade="all, delete")


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    status_code = Column(int)
    response = Column(str)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"))
