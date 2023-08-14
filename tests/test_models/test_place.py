#!/usr/bin/python3
import unittest
from models.place import Place
"""
Unittest  for Place class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for Place class '''

    def test_place(self):
        ''' test class '''
        self.place = Place()
