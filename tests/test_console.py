#!/usr/bin/python3

import unittest
from unittest.mock import patch
import io
import os
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.storage = FileStorage()
        self.storage.reload()  # Load existing instances

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)  # Ensure something is printed (the ID)

    def test_show(self):
        """Test show command"""
        model = BaseModel()
        model.save()
        model_id = model.id

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd(f"show BaseModel {model_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(model_id, output)  # Output should contain the ID

    def test_destroy(self):
        """Test destroy command"""
        model = BaseModel()
        model.save()
        model_id = model.id

        self.console.onecmd(f"destroy BaseModel {model_id}")
        self.assertNotIn(f"BaseModel.{model_id}", self.storage.all())

    def test_all(self):
        """Test all command"""
        model = BaseModel()
        model.save()

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("all BaseModel")
            output = fake_out.getvalue().strip()
            self.assertIn(model.id, output)  # Output should contain the ID

    def test_update(self):
        """Test update command"""
        model = BaseModel()
        model.save()
        model_id = model.id
        self.console.onecmd(f"update BaseModel {model_id} first_name \"John\"")

        # Verify the update
        updated_model = self.storage.all()[f"BaseModel.{model_id}"]
        self.assertEqual(updated_model.first_name, "John")


if __name__ == '__main__':
    unittest.main()
