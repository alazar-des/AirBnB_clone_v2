#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import String, Column, Integer, ForeignKey


class Amenity(BaseModel, Base):
    if storage_t == 'db':
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
    else:
        name = ""
