#!/usr/bin/python3
import unittest
from models.review import Review
"""
Unittest for Review class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for review class '''

    def test_review(self):
        ''' test class '''
        self.review = Review()
