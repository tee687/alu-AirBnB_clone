#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel."""

    def test_instantiation(self):
        """Test instantiation."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method."""
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)


if __name__ == "__main__":
    unittest.main()
