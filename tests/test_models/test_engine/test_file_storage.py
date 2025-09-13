#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel   # import your model(s) here

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    # Dictionary to map class names to classes
    classes = {
        "BaseModel": BaseModel,
        # later, you can add "User": User, etc.
    }

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the __objects to a JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """Loads the objects from the JSON file, if it exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value['__class__']
                    cls = self.classes.get(cls_name)
                    if cls:   # only recreate if class is known
                        self.new(cls(**value))

