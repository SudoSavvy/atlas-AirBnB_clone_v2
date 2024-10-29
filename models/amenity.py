from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('user_id', String(60), ForeignKey('users.id'), primary_key=True)
)
class Amenity(BaseModel):
    __tablename__ = 'amenities'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary="place_amenity", back_populates="amenities")
