#!/usr/bin/python3
"""FileStorage engine for serialization/deserialization."""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    __classes = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
            for key, obj_data in data.items():
                cls_name = obj_data["__class__"]
                cls = FileStorage.__classes.get(cls_name)
                if cls:
                    FileStorage.__objects[key] = cls(**obj_data)
        except FileNotFoundError:
            pass
