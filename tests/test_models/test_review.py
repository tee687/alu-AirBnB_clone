#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for Review."""

    def test_attributes(self):
        """Test Review default attributes."""
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")


if __name__ == "__main__":
    unittest.main()

