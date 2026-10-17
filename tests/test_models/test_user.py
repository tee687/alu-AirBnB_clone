#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for User."""

    def test_attributes(self):
        """Test User default attributes."""
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")


if __name__ == "__main__":
    unittest.main()
