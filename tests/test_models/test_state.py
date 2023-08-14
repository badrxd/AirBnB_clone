#!/usr/bin/python3
import unittest
from models.state import State
"""
Unittest for State class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for State class '''

    def test_state(self):
        ''' test class '''
        self.state = State()
