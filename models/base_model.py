#!/usr/bin/python3
"""Defines Base Model"""
from datetime import datetime
import uuid


class BaseModel:
    """Represents a Base Model"""

    def __init__(self):
        """Initializes data"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Prints string representation"""
        return "[{}] ({}) <{}>".format(
                str(self.__class__.__name__), self.id, str(self.__dict__))

    def save(self):
        """Updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
            __dict__ of the instance.
        """
        return vars(self)
