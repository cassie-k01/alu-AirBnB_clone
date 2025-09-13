#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up a new BaseModel instance for testing."""
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_initialization(self):
        """Test that a BaseModel instance is initialized correctly."""
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test that to_dict method gives a dict with the right attributes."""
        model_dict = self.model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)

    def test_to_dict_datetime_is_str(self):
        """Test that datetime fields in to_dict are strings."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str(self):
        """Test the string representation of BaseModel."""
        model_str = str(self.model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(self.model.id, model_str)

    def test_save(self):
        """Test that save updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_kwargs_initialization(self):
        """Test creating a new instance using kwargs """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.name, "My First Model")
        self.assertEqual(new_model.my_number, 89)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
