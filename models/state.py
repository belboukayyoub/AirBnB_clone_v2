#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import type_storage
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if type_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of related cities to the current state"""
            from models import storage
            cities = storage.all(City)
            related_cities = []
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities