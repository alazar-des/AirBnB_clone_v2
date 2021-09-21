#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='states')
    else:
        name = ""

        @property
        def cities(self):
            """getter for cityies with the same state with the current instance
            """
            city_list = []
            all_cities = models.storage.all(City)
            for key, city in all_cities.items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
