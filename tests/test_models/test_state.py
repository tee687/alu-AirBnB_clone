#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for State."""

    def test_attributes(self):
        """Test State default attributes."""
        s = State()
        self.assertEqual(s.name, "")


if __name__ == "__main__":
    unittest.main()

