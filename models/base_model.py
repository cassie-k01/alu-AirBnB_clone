#!/usr/bin/python3
"""
Define 'BaseModel' class
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # Generate a new ID
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            from models import storage
            storage.new(self)  # Register the new instance with storage

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()  # Save the current state to the JSON file

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__
        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()
        return dict_representation

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
