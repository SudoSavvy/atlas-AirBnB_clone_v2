#!/usr/bin/python3
"""FileStorage class for AirBnB project"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or filtered by class"""
        if cls:
            return {key: val for key, val in self.__objects.items() if isinstance(val, cls)}
        return self.__objects


    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects, handling empty file case."""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as f:
                    objects_dict = json.load(f)
                    for key, value in objects_dict.items():
                        cls_name = value["__class__"]
                        self.__objects[key] = eval(cls_name)(**value)
            except json.JSONDecodeError:
                # If the file is empty or invalid, leave __objects as an empty dict
                self.__objects = {}

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

