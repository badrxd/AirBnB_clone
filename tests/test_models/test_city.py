#!/usr/bin/python3
import unittest
from models.city import City
"""
Unittest for City class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for city class '''

    def test_city(self):
        ''' instantiates class '''
        self.city = City()
