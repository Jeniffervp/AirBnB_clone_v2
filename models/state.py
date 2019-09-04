#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:

        @property
        def cities(self):

            lista = []
            obje = models.storage.all(City)

            for key, val in obje.items():
                if val.state_id == self.id:
                    lista.append(val)
            return lista
