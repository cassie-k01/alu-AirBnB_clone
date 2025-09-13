#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):
    """Comprehensive tests for the User class."""

    def setUp(self):
        """Create a fresh User instance before each test."""
        self.user = User()

    def test_inheritance(self):
        """User should inherit from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_default_attributes(self):
        """User defaults: email, password, first_name, last_name all exist and are empty strings."""
        for attr in ("email", "password", "first_name", "last_name"):
            self.assertTrue(hasattr(self.user, attr))
            self.assertEqual(getattr(self.user, attr), "")
            self.assertIsInstance(getattr(self.user, attr), str)

    def test_to_dict_contains_class(self):
        """to_dict() must include a __class__ key equal to 'User'."""
        u_dict = self.user.to_dict()
        self.assertIn("__class__", u_dict)
        self.assertEqual(u_dict["__class__"], "User")

    def test_to_dict_datetime_format(self):
        """to_dict() must convert datetimes to ISO-format strings."""
        u_dict = self.user.to_dict()
        for key in ("created_at", "updated_at"):
            self.assertIsInstance(u_dict[key], str)
            # Should parse without error
            datetime.fromisoformat(u_dict[key])

    def test_save_updates_updated_at(self):
        """Calling save() must bump the updated_at timestamp."""
        old = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old)
        self.assertGreater(self.user.updated_at, old)

if __name__ == "__main__":
    unittest.main()
