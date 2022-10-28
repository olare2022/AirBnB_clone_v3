<<<<<<< HEAD
#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity
=======
#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
<<<<<<< HEAD
        '''
                Implementation for the Amenities.
            '''
            __tablename__ = "amenities"
                if getenv("HBNB_TYPE_STORAGE") == "db":
                            name = Column(String(128), nullable=False)
                                    place_amenities = relationship("Place", secondary=place_amenity,
                                                                                                          back_populates="amenities")
                                        else:
                                                    name = ""
=======
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
