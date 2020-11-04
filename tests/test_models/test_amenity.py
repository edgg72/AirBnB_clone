#!/usr/bin/python3
"""
Test Amenity
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testamenity(unittest.TestCase):
    """
    For Unittest
    """

    def test_class(self):
        """"
        test class
        """
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        """
        test father
        """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_amenity(self):
        """
        Test attributes of Class Amenity
        """
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')
