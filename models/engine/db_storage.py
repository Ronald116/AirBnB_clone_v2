#!/usr/bin/python3
"""
Database storage linked to MySQL database
"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
nametoclass = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize database"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd,
                                                   host, database)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""

        if not self.__session:
            self.reload()
        objects = {}
        if type(cls) == str:
            cls = nametoclass.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in nametoclass.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if not self.__session:
            self.reload()
        else:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Dispose of the current session"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieve an object"""
        if cls is not None and type(cls) is str and id is not None and\
           type(id) is str and cls in nametoclass:
            cls = nametoclass[cls]
            result = self.__session.query(cls).filter(cls.id == id).first()
            return result
        else:
            return None

    def count(self, cls=None):
        """Count number of objects in storage"""
        total = 0
        if type(cls) == str and cls in nametoclass:
            cls = nametoclass[cls]
            total = self.__session.query(cls).count()
        elif cls is None:
            for cls in nametoclass.values():
                total += self.__session.query(cls).count()
        return total
