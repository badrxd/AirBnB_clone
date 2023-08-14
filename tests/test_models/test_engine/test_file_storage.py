#!/usr/bin/python3
"""
FileStorage test
"""
from models import storage
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class FileStorageTestCase(unittest.TestCase):
    """ Unittest for FileStorage class """

    def test_file_access(self):
        ''' test read and write access permissions '''

        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exitt = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exitt)
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_FileStorage_class(self):
        """ creat object """
        stg2 = FileStorage()
        self.assertIsInstance(stg2, FileStorage)
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_mtd(self):
        """ test the all methode """

        stg2 = FileStorage()
        self.assertIsInstance(stg2.all(), dict)
        self.assertIsInstance(stg2, FileStorage)
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        """ test the new  methode """

        stg = BaseModel()
        stg2 = FileStorage()
        key = "{}.{}".format(stg.__class__.__name__, stg.id)
        self.assertIn(key, stg2.all())
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_save(self):
        """ test the save methode """

        stg = BaseModel()
        stg.name = "badr"
        stg2 = FileStorage()
        stg.save()
        with open(FileStorage._FileStorage__file_path, "r") as json_file:
            objects = json.load(json_file)
        key = "{}.{}".format(stg.__class__.__name__, stg.id)
        self.assertIn(key, objects)
        self.assertEqual(stg.name, objects[key]['name'])
        self.assertNotEqual(stg.updated_at, objects[key]['updated_at'])
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_reload(self):
        """ test the reload methode """
        stg = BaseModel()
        stg.name = "badr xd"
        stg2 = FileStorage()
        stg2.new(stg)
        stg2.save()
        FileStorage._FileStorage__objects = {}
        self.assertTrue(len(FileStorage._FileStorage__objects) == 0)
        stg2.reload()
        key = "{}.{}".format(stg.__class__.__name__, stg.id)
        self.assertIn(key, stg2.all())
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
