#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def setUp(self):
        """Create a fresh City instance before each test."""
        self.city = City()

    def test_inheritance(self):
        """City should inherit from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_default_attributes(self):
        """City requires 'state_id' and 'name' with empty string defaults."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_to_dict_contains_class(self):
        """to_dict() must include a '__class__' key equal to 'City'."""
        city_dict = self.city.to_dict()
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_to_dict_datetime_format(self):
        """to_dict() must convert timestamps to ISO-format strings."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        datetime.fromisoformat(city_dict["created_at"])
        datetime.fromisoformat(city_dict["updated_at"])

    def test_save_updates_updated_at(self):
        """Calling save() must update the 'updated_at' timestamp."""
        old_updated = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated)
        self.assertGreater(self.city.updated_at, old_updated)


if __name__ == "__main__":
    unittest.main()
