#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete-orphan')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing city"""
        super().__init__(*args, **kwargs)
