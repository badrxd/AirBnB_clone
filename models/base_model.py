#!/usr/bin/python3
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel att.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key and value of attributes.
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        the_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    self.__dict__[k] = datetime.strptime(v, the_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """methode updates the public instance attribute :updated_at,
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """methode returns a copy of dictionary containing
        all keys/values of __dict__ of the instance
        """

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    def __str__(self):
        """Return the str representation of the BaseModel instance."""

        classname = self.__class__.__name__
        return("[{}] ({}) {}".format(classname, self.id, self.__dict__))
