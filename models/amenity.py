from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary="place_amenity", back_populates="amenities")

