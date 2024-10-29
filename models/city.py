#!/usr/bin/python3
""" city class defitions """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """Represents a City for a MySQL database."""
    __tablename__ = 'cities'

    id = Column(String(60), primary_key=True)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Relationship with Place (no backref or specify a unique name)
    places = relationship('Place', back_populates='city')  # Use back_populates instead of backref