#!/usr/bin/python3
"""Base Model"""

from models import storage
import json
import uuid
from datetime import datetime



class BaseModel:
    """
    public instance attrs for BaseModel go here
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel
        """

        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            kwargs.pop("__class__")
            for key, value in kwargs.items():
                if key is "created_at" or key is "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeFormat)
                else:
                    setattr(self, key, value)

        if "id" in kwargs.keys():
            self.id = kwargs["id"]

    def __str__(self):
        """
        returns a string representation of the BaseModel instance
        """
        className = self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """
        updates the instance's updated_at attr with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing keys/values of the instance's __dict__
        """
        thisDict = self.__dict__.copy()
        thisDict["created_at"] = datetime.isoformat((self.created_at))
        thisDict["updated_at"] = datetime.isoformat((self.updated_at))
        thisDict["__class__"] = self.__class__.__name__
        return thisDict
