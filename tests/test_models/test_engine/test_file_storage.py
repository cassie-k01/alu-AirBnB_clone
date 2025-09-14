#!/usr/bin/python3

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)
        self.test_file = "file.json"

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        FileStorage._FileStorage__objects = {}

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects"""
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save() creates file.json"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.test_file))

    def test_reload_restores_objects(self):
        """Test that reload() repopulates __objects"""
        self.storage.save()
        FileStorage._FileStorage__objects = {}  # Clear manually
        self.storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
