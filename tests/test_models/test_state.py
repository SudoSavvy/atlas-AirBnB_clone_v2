#!/usr/bin/python3
import unittest
from models.state import State
from models import storage
import MySQLdb

class TestState(unittest.TestCase):

    @unittest.skipIf(type(storage).__name__ != 'DBStorage', "DBStorage test only")
    def test_create_state_db(self):
        """Test state creation in DBStorage"""
        db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        cursor = db.cursor()

        # Check state count before creation
        cursor.execute("SELECT COUNT(*) FROM states;")
        count_before = cursor.fetchone()[0]

        # Create state
        state = State(name="California")
        state.save()

        # Check state count after creation
        cursor.execute("SELECT COUNT(*) FROM states;")
        count_after = cursor.fetchone()[0]

        self.assertEqual(count_after, count_before + 1)
        cursor.close()
        db.close()

    @unittest.skipIf(type(storage).__name__ != 'FileStorage', "FileStorage test only")
    def test_create_state_file(self):
        """Test state creation in FileStorage"""
        state = State(name="California")
        state.save()
        states = storage.all(State)
        self.assertIn(state, states.values())
