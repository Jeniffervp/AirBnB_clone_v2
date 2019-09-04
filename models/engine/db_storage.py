#!/usr/bin/python3
""" This file manage all the database """

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ this class will contain all the manages of database
    """

    __engine = None
    __session = None

    def __init__(self):
        """ this contain the definition of environ variables
            the creation of engine and the reload that if
            the test is equal to the environment should drop
            down all the tables.
        """

        envi = getenv('HBNB_ENV')
        my_user = getenv('HBNB_MYSQL_USER')
        my_psswd = getenv('HBNB_MYSQL_PWD')
        my_host = getenv('HBNB_MYSQL_HOST')
        my_datab = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(my_user, my_psswd,
                                              my_host, my_datab),
                                      pool_pre_ping=True)
        self.reload()

        if 'test' == envi:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ this contain the filter that depend of the class
            that is specified
        """
        dicti = {}
        list_cls = []

        if cls is None:
            list_cls += self.__session.query(State).all()
            list_cls += self.__session.query(City).all()
            list_cls += self.__session.query(User).all()
            list_cls += self.__session.query(Place).all()
            list_cls += self.__session.query(Review).all()
            list_cls += self.__session.query(Amenity).all()

        else:
            list_cls = self.__session.query(cls).all()

        for var in list_cls:
            k = type(var).__name__ + '.' + var.id
            dicti[k] = var

        return dicti

    def new(self, obj):
        """ add the object to session """

        self.__session.add(obj)

    def save(self):
        """ commit all the changes to session """

        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the session """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ This function create all the tables and the session """

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """ Close session """
        self.__session.close()
