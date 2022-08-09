#!/usr/bin/python3
"""
class BaseModel
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A class that acts as a superclass or
    parent class to all other classes"""

    def __init__(self, *args, **kwargs):
        """BaseModel class initialization"""

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                """sets values to attributes"""
                if key != "__class__":
                    setattr(self, key, value)

            """Convert date and time from string to the preferred format"""
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            elif hasattr(self, "updated_at")and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representation of an instance"""
        return "[{:s}] ({:s}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at attribute with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns all instance attribute in a dictionary form"""
        this_dict = self.__dict__.copy()
        this_dict["__class__"] = type(self).__name__
        this_dict["created_at"] = this_dict["created_at"].isoformat()
        this_dict["updated_at"] = this_dict["created_at"]
        return this_dict
