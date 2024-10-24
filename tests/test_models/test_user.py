#!/usr/bin/python3import unittest
from models.user import User
from models import storage
import MySQLdb

class TestUser(unittest.TestCase):

    @unittest.skipIf(type(storage).__name__ != 'DBStorage', "DBStorage test only")
    def test_create_user_db(self):
        """Test user creation in DBStorage"""
        db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        cursor = db.cursor()

        # Check user count before creation
        cursor.execute("SELECT COUNT(*) FROM users;")
        count_before = cursor.fetchone()[0]

        # Create user
        user = User(email="test@user.com", password="test_pwd")
        user.save()

        # Check user count after creation
        cursor.execute("SELECT COUNT(*) FROM users;")
        count_after = cursor.fetchone()[0]

        self.assertEqual(count_after, count_before + 1)
        cursor.close()
        db.close()

    @unittest.skipIf(type(storage).__name__ != 'FileStorage', "FileStorage test only")
    def test_create_user_file(self):
        """Test user creation in FileStorage"""
        user = User(email="test@user.com", password="test_pwd")
        user.save()
        users = storage.all(User)
        self.assertIn(user, users.values())

    def test_create_user_missing_email(self):
        """Test user creation fails with missing email"""
        with self.assertRaises(ValueError):
            User(password="test_pwd").save()

    def test_create_user_missing_password(self):
        """Test user creation fails with missing password"""
        with self.assertRaises(ValueError):
            User(email="test@user.com").save()
