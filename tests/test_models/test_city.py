#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for City."""

    def test_attributes(self):
        """Test City default attributes."""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


if __name__ == "__main__":
    unittest.main()

