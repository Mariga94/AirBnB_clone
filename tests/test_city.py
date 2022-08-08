#!/usr/bin/python3
"""
Unittest for Place model class
"""
from models.base_model import BaseModel
import unittest
import os
from models.city import City


class test_City(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ """
        cls.city1 = City()
        cls.city1.state_id = "047"
        cls.city1.name = "Nairobi"

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """ """
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_doc(self):
        """ """
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """ """
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        """  """
        self.assertTrue(type(self.city1.state_id), str)
        self.assertTrue(type(self.city1.name), str)

    def test_save(self):
        """ """
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unnittest.main()
