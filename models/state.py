#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import datetime  #1


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states',
                              cascade='all, delete')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize state"""
        super().__init__(*args, **kwargs)
        #2
        if 'created_at' not in kwargs:
            self.creatd_at = datetime.datetime.now()

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            city_values = models.storage.all('City').values()
            list_city = []
            for city in city_values:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
