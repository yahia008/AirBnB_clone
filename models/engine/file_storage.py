#!/usr/bin/python3
"""Creating the FileStorage class."""
import json
from models.base_model import BaseModel
from os import path


class FileStorage:
    """This indicates an abstract storage engine.

    Attr:
        __file_path (str): The filename used for storing objects.
        __objects (dict): A collection of intantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gives the object dictionary."""
        return FileStorage.__objects

    def new(sef, obj):
        """Add the "obj" with the key "<obj_class_name>.id"
        into the "__objects" dictionary.
        """
        clsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
