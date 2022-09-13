#!/usr/bin/python3
"""
Contains a class FileStorage that serializes instances to JSON file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represents a file storage

    Attributes:
        __file_path (str):
        __objects (dict):
    """
    __file_path = "file.json"
    __objects = {}

    classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                    }

    def all(self):
        """Returns a dictionay of instatiated __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key < obj class name>.id"""
        self.__objects["{}.{}".format(__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dictionary = {}
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the
            JSON file (__file_path) exists; otherwise, do nothing.
        """
        try:
            dicts = {}
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                dicts = json.load(f)
            for key, value in dicts.items():
                self.all()[key] = self.classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
