#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
import unittest
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity


class TestPlaceAmenity(unittest.TestCase):
    """ Test for the Place and Amenity relationship """

    def setUp(self):
        """ Set up a test environment """
        self.state = State(name="California")
        self.state.save()

        self.city = City(state_id=self.state.id, name="San Francisco")
        self.city.save()

        self.user = User(email="john@snow.com", password="johnpwd")
        self.user.save()

        self.place = Place(user_id=self.user.id, city_id=self.city.id, name="House")
        self.place.save()

        self.amenity1 = Amenity(name="Wifi")
        self.amenity1.save()

        self.amenity2 = Amenity(name="Cable")
        self.amenity2.save()

    def tearDown(self):
        """ Clean up after each test """
        storage.delete(self.place)
        storage.delete(self.city)
        storage.delete(self.state)
        storage.delete(self.user)
        storage.delete(self.amenity1)
        storage.delete(self.amenity2)

    def test_place_amenities_relationship(self):
        """ Test that amenities can be added to a place """
        self.place.amenities.append(self.amenity1)
        self.place.amenities.append(self.amenity2)

        self.assertIn(self.amenity1, self.place.amenities)
        self.assertIn(self.amenity2, self.place.amenities)

    def test_place_amenities_save_to_db(self):
        """ Test that amenities are saved correctly in the database """
        self.place.amenities.append(self.amenity1)
        self.place.save()
        
        # Check if the relationship is saved in the place_amenity table
        amenities = storage.all(Amenity)
        place_amenities = [amenity.id for amenity in self.place.amenities]
        self.assertIn(self.amenity1.id, place_amenities)

if __name__ == "__main__":
    unittest.main()
