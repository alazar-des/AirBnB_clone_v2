#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
import models
from sqlalchemy.orm import relationship


if models.storage_t == 'db':
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True)
                          )

class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_t == 'db':
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all,delete", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter for review with the same state with the current instance
            """
            review_list = []
            all_review = models.storage.all(Review)
            for review in all_reviews:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter for amenity with the same place_id
            with the current instance
            """
            amenities_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities:
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """setter for amenity
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.amenity_ids)
