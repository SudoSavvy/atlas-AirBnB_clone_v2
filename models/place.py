#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    extend_existing=True  # Add this line
)

class Place(BaseModel, Base):
    """Represents a Place for a MySQL database."""
    __tablename__ = 'places'

    # Foreign key linking to User
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)  # Make sure this is here

    # Relationship with Amenity
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

    @property
    def amenities(self):
        """Getter for amenities in FileStorage mode."""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """Setter for amenities in FileStorage mode."""
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
