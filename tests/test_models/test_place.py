#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class."""

    def setUp(self):
        """Create a fresh Place instance before each test."""
        self.place = Place()

    def test_inheritance(self):
        """Place should inherit from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_default_attributes(self):
        """Place defaults: check attribute existence and type."""
        attrs = {
            "city_id": str,
            "user_id": str,
            "name": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list
        }
        for attr, attr_type in attrs.items():
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.place, attr))
                self.assertIsInstance(getattr(self.place, attr), attr_type)

    def test_to_dict_contains_class(self):
        """to_dict() must include a '__class__' key equal to 'Place'."""
        place_dict = self.place.to_dict()
        self.assertIn("__class__", place_dict)
        self.assertEqual(place_dict["__class__"], "Place")

    def test_to_dict_datetime_format(self):
        """to_dict() must convert datetimes to ISO-format strings."""
        place_dict = self.place.to_dict()
        for key in ("created_at", "updated_at"):
            self.assertIsInstance(place_dict[key], str)
            # parsing back to datetime should not raise
            datetime.fromisoformat(place_dict[key])

    def test_save_updates_updated_at(self):
        """Calling save() must update the 'updated_at' timestamp."""
        old_updated = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated)
        self.assertGreater(self.place.updated_at, old_updated)


if __name__ == "__main__":
    unittest.main()
