#!/usr/bin/python3
<<<<<<< HEAD
'''
    Implementation of the User class which inherits from BaseModel
'''
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
=======
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
=======
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
