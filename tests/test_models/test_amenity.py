#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def setUp(self):
        """Create a fresh Amenity instance before each test."""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Amenity should inherit from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_default_attribute(self):
        """Amenity should have 'name' defaulting to an empty string."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict_contains_class(self):
        """to_dict() must include a '__class__' key equal to 'Amenity'."""
        amenity_dict = self.amenity.to_dict()
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_to_dict_datetime_format(self):
        """to_dict() must convert timestamps to ISO-format strings."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)
        # Confirm they parse back into datetime objects
        datetime.fromisoformat(amenity_dict["created_at"])
        datetime.fromisoformat(amenity_dict["updated_at"])

    def test_save_updates_updated_at(self):
        """Calling save() must update the 'updated_at' timestamp."""
        old_updated = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated)
        self.assertGreater(self.amenity.updated_at, old_updated)


if __name__ == "__main__":
    unittest.main()
