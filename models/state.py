#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """The state class, contains name and linked cities"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    if models.storage_type != 'db':
        @property
        def cities(self):
            """Getter for cities if using FileStorage."""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
