#!/usr/bin/python3
"""
Test State
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Teststate(unittest.TestCase):
    """
    For Unittest
    """

    def test_class(self):
        """
        test class
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """
        test father
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        my_state.name = "Antioquia"
        self.assertEqual(my_state.name, 'Antioquia')
