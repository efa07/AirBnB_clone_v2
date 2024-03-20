#!/usr/bin/python3
""" Tests for amenity """

import models
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
# from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ Class of Amenity
    Attributes:
        name: entry name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', secondary='place_amenity')
