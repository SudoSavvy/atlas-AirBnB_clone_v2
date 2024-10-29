#!/usr/bin/python3
""" file storage testing module """
import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
class test_fileStorage(unittest.TestCase):
    """ file storage method test class """
    def setUp(self):
        """ start test environ """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ remove storage file at test end """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ ensure objects is initally empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ ensure objects are added correctly """
        new = BaseModel()
        for obj in storage.all().values():
            self.assertTrue(new is obj)

    def test_all(self):
        """ objects gets returned correctly """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ test file saving correctly or not """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ test data getting saved """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_reload_empty(self):
        """ loading from empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ null if file is non existant """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ basemodel save and exist """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ ensures file path is a string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ makes sure obj dictornary handling """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ ensures keys are formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            self.assertEqual(key, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ ensures stored files are created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)