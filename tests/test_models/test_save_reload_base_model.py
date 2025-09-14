#!/usr/bin/python3

import unittest
from models import storage
from models.base_model import BaseModel

class TestSaveReloadBaseModel(unittest.TestCase):
    def test_save_and_reload(self):
        obj = BaseModel()
        obj.name = "Test"
        obj.save()

        # Clear in-memory objects
        storage._FileStorage__objects = {}

        # Reload from file
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, "Test")

if __name__ == "__main__":
    unittest.main()
