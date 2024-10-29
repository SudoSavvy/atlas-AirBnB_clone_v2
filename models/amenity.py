from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # Many-to-Many relationship with Place
    place_amenities = relationship('Place', secondary='place_amenity', viewonly=False)