#!/usr/bin/python3
"""Defines a class City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """A City class that inherits from State and Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
            unique=True, nullable=False,
            autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    #state = relationship('State', back_populates='cities')
