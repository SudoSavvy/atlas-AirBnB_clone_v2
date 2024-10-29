#!/usr/bin/python3
""" this is the user definitions """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """ class that handles user info """
    __tablename__ = "users"
    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    # Relationships
    places = relationship("Place", secondary="place_amenity", back_populates="users")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")