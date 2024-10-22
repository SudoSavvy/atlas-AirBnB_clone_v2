#!/usr/bin/python3
"""class state"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """class that represents the state values"""
    if models.storage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """getter method that returns the list of city objects linked to
        the current state"""
        city_list = []
        if models.storage_t != "db":
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
        return city_list