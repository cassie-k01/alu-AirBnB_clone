#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime

class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def setUp(self):
        """Create a fresh State instance before each test."""
        self.state = State()

    def test_inheritance(self):
        """State should inherit from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_default_attribute(self):
        """State should have 'name' attribute defaulting to an empty string."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.name, str)

    def test_to_dict_contains_class(self):
        """to_dict() must include a '__class__' key equal to 'State'."""
        state_dict = self.state.to_dict()
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_to_dict_datetime_format(self):
        """to_dict() must convert datetimes to ISO-format strings."""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        # Verify they parse back into datetime objects
        datetime.fromisoformat(state_dict["created_at"])
        datetime.fromisoformat(state_dict["updated_at"])

    def test_save_updates_updated_at(self):
        """Calling save() must update the 'updated_at' timestamp."""
        old_updated = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated)
        self.assertGreater(self.state.updated_at, old_updated)

if __name__ == "__main__":
    unittest.main()
