#!/usr/bin/python3
""" Unittest for User class """
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Unittest for User class """
    @classmethod
    def setUpClass(cls):
        """ creat object """
        cls.my_user = User()
        cls.my_user.first_name = "badr"
        cls.my_user.last_name = "xd"
        cls.my_user.email = "badr@gmail.com"
        cls.my_user.password = "badr"
