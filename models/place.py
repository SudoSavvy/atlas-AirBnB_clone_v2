#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('place_id', Integer, ForeignKey('places.id'), primary_key=True)
)


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

class Place(Base):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    users = relationship("User", secondary=place_amenity, back_populates="places")

