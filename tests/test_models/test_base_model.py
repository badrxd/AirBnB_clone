#!/usr/bin/python3
"""
test
"""
import json
import unittest
from models.base_model import BaseModel
from time import sleep
from datetime import datetime


class BaseModelTestCase(unittest.TestCase):
    """ Unittest for BaseModel class """

    def chek_base_class(self):
        """ creat object """
        instance = BaseModel()

    def test_checking_init(self):
        """ test Class attributes """
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "updated_at"))
        self.assertTrue(hasattr(instance, "created_at"))
        instance.name = "bro"
        self.assertTrue(hasattr(instance, "name"))
        self.assertEqual("bro", instance.name)

    def test_checking_save(self):
        """ testing save methode """

        instance = BaseModel()
        updated_at = instance.updated_at
        sleep(0.06)
        instance.save()
        self.assertGreater(instance.updated_at, updated_at)

    def test_checking_to_dict(self):
        """ testing to dict methode """

        instance = BaseModel()
        dic = instance.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertEqual(instance.updated_at.isoformat(), dic["updated_at"])
        self.assertIn("__class__", dic)
        self.assertEqual(instance.__class__.__name__, dic["__class__"])

    def test_checking_str(self):
        """ testing str methode """

        instance = BaseModel()
        classname = instance.__class__.__name__
        msg = "[{}] ({}) {}".format(classname, instance.id, instance.__dict__)
        self.assertEqual(msg, str(instance))


if __name__ == '__main__':
    unittest.main()
