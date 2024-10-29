#!/usr/bin/python3
""" tests console """
import os
import uuid
import unittest
import models
import console
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models.state import State


@unittest.skipIf(isinstance(models.storage, DBStorage), "Testing DBStorage")
class TestHBNBCommand(unittest.TestCase):
    """ unittesting for console"""
    @classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(test_cls):
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass
        del test_cls.HBNB
        if type(models.storage) is DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Amenity")
            new_amenity = test.getvalue().strip()

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Amenity")
            new_amenity = test.getvalue().strip()

    def test_create_kwargs(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create User first_name="John"\
                             email="john@example.com" password="1234"')
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            self.assertIn(new_user, test.getvalue())
            self.assertIn("'first_name': 'John'", test.getvalue())
            self.assertIn("'email': 'john@example.com'", test.getvalue())
            self.assertNotIn("'last_name': 'Snow'", test.getvalue())
            self.assertIn("'password': '1234'", test.getvalue())


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'test DB mode')
class TestHBNBComDB(unittest.TestCase):
    """ testing for database connections"""

    @classmethod
    def setUpClass(cls):
        cls.cli = HBNBCommand()

    def setUp(self):
        pass

    def test_storage(self):
        self.assertIsInstance(console.storage, DBStorage)
        obj = State()
        obj.name = "California"
        obj.save()
        self.assertEqual(type(obj), State)

    def test_crt_dbs(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("create State name='California'")
            ca = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("all State")
            self.assertIn(ca, f.getvalue())


if __name__ == '__main__':
    unittest.main()
