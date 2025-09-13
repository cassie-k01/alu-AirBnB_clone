#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime

class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def setUp(self):
        """Create a fresh Review instance before each test."""
        self.review = Review()

    def test_inheritance(self):
        """Review should inherit from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_default_attributes(self):
        """Review defaults: place_id, user_id, text all exist and are empty strings."""
        attrs = {
            "place_id": str,
            "user_id": str,
            "text": str,
        }
        for attr, attr_type in attrs.items():
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.review, attr))
                self.assertEqual(getattr(self.review, attr), "")
                self.assertIsInstance(getattr(self.review, attr), attr_type)

    def test_to_dict_contains_class(self):
        """to_dict() must include a '__class__' key equal to 'Review'."""
        rev_dict = self.review.to_dict()
        self.assertIn("__class__", rev_dict)
        self.assertEqual(rev_dict["__class__"], "Review")

    def test_to_dict_datetime_format(self):
        """to_dict() must convert timestamps to ISO-format strings."""
        rev_dict = self.review.to_dict()
        for key in ("created_at", "updated_at"):
            self.assertIsInstance(rev_dict[key], str)
            # ensure the timestamp string can be parsed back to datetime
            datetime.fromisoformat(rev_dict[key])

    def test_save_updates_updated_at(self):
        """Calling save() must update the 'updated_at' timestamp."""
        old_updated = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated)
        self.assertGreater(self.review.updated_at, old_updated)

if __name__ == "__main__":
    unittest.main()
