#!/usr/bin/python3
"""
Unittest for Place model class
"""
from models.base_model import BaseModel
import unittest
import os
from models.place import Place


class test_Place(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ """
        cls.place1 = Place()
        cls.place1.city_id = "Nairobi123"
        cls.place1.user_id = "Uhuru123"
        cls.place1.name = "Lenya"
        cls.place1.description = "State House"
        cls.place1.number_rooms = 0
        cls.place1.number_bathrooms = 0
        cls.place1.max_guest = 0
        cls.place1.price_by_night = 0
        cls.place1.latitude = 0.0
        cls.place1.longitude = 0.0
        cls.place1.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """ """
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_checking_for_doc(self):
        """ """
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """ """
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)

    def test_attributes_are_strings(self):
        """  """
        self.assertTrue(type(self.place1.city_id), str)
        self.assertTrue(type(self.place1.user_id), str)
        self.assertTrue(type(self.place1.name), str)
        self.assertTrue(type(self.place1.description), str)
        self.assertTrue(type(self.place1.number_rooms), str)
        self.assertTrue(type(self.place1.number_bathrooms), str)
        self.assertTrue(type(self.place1.max_guest), str)
        self.assertTrue(type(self.place1.price_by_night), str)
        self.assertTrue(type(self.place1.latitude), str)
        self.assertTrue(type(self.place1.longitude), str)
        self.assertTrue(type(self.place1.amenity_ids), str)

    def test_save(self):
        """ """
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.place1), True)


if __name__ == "__main__":
    unnittest.main()
