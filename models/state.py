#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class, contains state name """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete-orphan',
                              backref='state')
    else:
        @property
        def cities(self):
            from models import storage
            list_cities = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
