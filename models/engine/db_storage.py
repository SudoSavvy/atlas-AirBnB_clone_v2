#!/usr/bin/python3
""" module for database handling """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ sql database storage solution definitions """
    __engine = None
    __session = None

    def __init__(self):
        """ creates engine and links to sql """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query all objects of determined class"""
        if cls is None:
            all_classes = [State, City, Amenity, Place, Review, User]
            temp = []
            for c in all_classes:
                temp.extend(self.__session.query(c).all())
        else:
            temp = self.__session.query(cls).all()
        new_dict = {}
        for obj in temp:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ add object to database session """
        self.__session.add(obj)

    def save(self):
        """ commit changes to current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object from current session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create required tables and their relevent sessions """
        Base.metadata.create_all(self.__engine)
        session_temp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_temp)
        self.__session = Session()

    def close(self):
        """ remove or close current session """
        self.__session.close()
