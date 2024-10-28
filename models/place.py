#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    extend_existing=True
)

class Place(BaseModel, Base):
    """Represents a Place for a MySQL database."""
    __tablename__ = 'places'

    # Add the foreign key for user
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Relationship with Amenity
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
