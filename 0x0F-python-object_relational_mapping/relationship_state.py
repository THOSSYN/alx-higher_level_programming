#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """Creates a class that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete-orphan",
                          back_populates="state")
