#!/usr/bin/python3
"""
test
"""
import json
import unittest
from io import StringIO
import sys
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """ class for base test """
    pass


if __name__ == '__main__':
    unittest.main()
