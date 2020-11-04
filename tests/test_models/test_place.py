#!/usr/bin/python3
"""Test Place"""
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
        """"
        test class
        """
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        """
        test father
        """
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))
