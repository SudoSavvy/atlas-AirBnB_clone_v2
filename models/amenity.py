#!/usr/bin/python3
"""This is the amenity class"""
import models
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    if models.storage == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Relationship with Place
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)