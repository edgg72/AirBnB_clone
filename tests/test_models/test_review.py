#!/usr/bin/python3
"""Test Review"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testpep8(unittest.TestCase):
    """
    For Unittest
    """

    def test_class(self):
        """
        test class
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """
        test father
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
