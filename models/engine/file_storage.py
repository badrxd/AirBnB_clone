#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent the FileStorage class.
    Attributes:
        __file_path (str): the filename where we will save objects to.
        __objects (dict): A dictionary of all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary of __objects. """

        return FileStorage.__objects

    def new(self, obj):
        """
        Set in the __objects obj with key <obj_class_name>.id
        Args:
             obj (obj): an object
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file __file_path. """

        objs = dict(FileStorage.__objects)
        obj_dict = {}
        for obj in objs.keys():
            obj_dict[obj] = objs[obj].to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """ Deserialize the JSON file __file_path to the __objects,
        if the file exists.
        """

        try:
            with open(FileStorage.__file_path, "r") as json_file:
                objects = json.load(json_file)
                for obj in objects.values():
                    class_name = obj.pop("__class__")
                    instance = eval(class_name)(**obj)
                    self.new(instance)
        except FileNotFoundError:
            return
