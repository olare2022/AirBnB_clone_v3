#!/usr/bin/python3
<<<<<<< HEAD
'''
    This module defines the BaseModel class
'''
from os import getenv
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("created_at"):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
            if not self.id:
                self.id = str(uuid.uuid4())

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
=======
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if hasattr(self, "_sa_instance_state"):
            del cp_dct["_sa_instance_state"]
        return (cp_dct)

    def delete(self):
        '''
            Deletes an object
        '''
=======
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
        models.storage.delete(self)
