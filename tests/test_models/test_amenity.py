#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity."""

    def test_attributes(self):
        """Test Amenity default attributes."""
        a = Amenity()
        self.assertEqual(a.name, "")


if __name__ == "__main__":
    unittest.main()

