#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""
Unittest Module for Amenity
"""


class AmenityTest(unittest.TestCase):
    """ Unittest for amenity class """

    def test_Amenity(self):
        """ test Class attributes """
        self.amenity = Amenity()
