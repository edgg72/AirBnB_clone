#!/usr/bin/python3
"""
File Storage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """File Storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        aux = {}
        for key, value in self.__objects.items():
            aux[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(aux, file, indent="")

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as file:
                for k, value in (json.load(file)).items():
                    self.__objects[k] = eval(value["__class__"] + "(**value)")
        except FileNotFoundError:
            pass
