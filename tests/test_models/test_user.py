#!/usr/bin/python3
""" Unittest for User class """
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Unittest for User class """

    def test_first_name(self):
        """ Test first name"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(type(user.first_name) == str)
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """ Test last name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertTrue(type(user.last_name) == str)
        self.assertEqual(user.last_name, "")

    def test_email(self):
        """ Test email"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(type(user.email) == str)
        self.assertEqual(user.email, "")

    def test_password(self):
        """Test password"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(type(user.password) == str)
        self.assertEqual(user.password, "")


if __name__ == "__main__":
    unittest.main()
