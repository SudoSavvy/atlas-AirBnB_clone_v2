#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    extend_existing=True
)

class Place(BaseModel):
    __tablename__ = 'places'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)

    amenities = relationship("Amenity", secondary="place_amenity", back_populates="places")
    users = relationship("User", secondary="place_amenity", back_populates="places")
