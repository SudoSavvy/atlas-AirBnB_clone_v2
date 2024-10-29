
#!/usr/bin/python3
""" unittests for 'models/engine/db_storage.py' """
import models
import pep8
import MySQLdb
import unittest
import os
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestDatabaseDocs(unittest.TestCase):
    """ checks documentation style of classes"""
    @classmethod
    def setUpClass(cls):
        """ DBStorage testing setup """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="Oklahoma")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="Tulsa", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="oofouchmybones@gmail.com", password="milk")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="Valhala")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="MiniFridge")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="Loved it")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """ DBStorage teardown test """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstrings(self):
        """ test all methods have docstrings """
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_attributes(self):
        """ test engine and session attributes exist """
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    def test_dbstorage_methods(self):
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_init(self):
        """ test starter """
        self.assertTrue(isinstance(self.storage, DBStorage))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_all(self):
        """ test default all method """
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_new(self):
        st = State(name="Oklahoma")
        self.storage.new(st)
        store = list(self.storage._DBStorage__session.new)
        self.assertIn(st, store)

    @unittest.skipIf(type(models.storage)
                     == FileStorage, "Testing FileStorage")
    def test_dbstorage_save(self):
        """ test save method """
        st = State(name="Oklahoma")
        self.storage.new(st)
        self.storage.save()
        query = self.storage._DBStorage__session.query(State).all()
        self.assertIn(st, query)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_delete(self):
        """ test delete method """
        st = State(name="Oklahoma")
        self.storage.new(st)
        key = "{}.{}".format(type(st).__name__, st.id)
        self.storage.save()
        self.storage.delete(st)
        self.assertNotIn(key, self.storage.all().keys())

    def test_dbstorage_reload(self):
        """ test reload method """
        st = State(name="Oklahoma")
        storage.new(st)
        storage.save()

        query = storage._DBStorage__session.query(State).all()
        self.assertIn(st, query)

        storage._DBStorage__session.close()
        storage.reload()

        query = storage._DBStorage__session.query(State).all()
        self.assertIn(st, query)


if __name__ == "__main__":
    unittest.main()
