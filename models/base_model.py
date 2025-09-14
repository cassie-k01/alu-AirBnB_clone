#!/usr/bin/python3
"""Define 'BaseModel' class"""
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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__
        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()
        return dict_representation

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
