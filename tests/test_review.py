#!/usr/bin/python3
"""
Unittest for Place model class
"""
from models.base_model import BaseModel
import unittest
import os
from models.review import Review


class test_Review(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ """
        cls.review1 = Review()
        cls.review1.place_id = "#001"
        cls.review1.user_id = "Peter"
        cls.review1.text = "good"

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.review1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """ """
        self.assertTrue(issubclass(self.review1.__class__, BaseModel), True)

    def test_checking_for_doc(self):
        """ """
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """ """
        self.assertTrue('id' in self.review1.__dict__)
        self.assertTrue('created_at' in self.review1.__dict__)
        self.assertTrue('updated_at' in self.review1.__dict__)
        self.assertTrue('place_id' in self.review1.__dict__)
        self.assertTrue('user_id' in self.review1.__dict__)
        self.assertTrue('text' in self.review1.__dict__)

    def test_attributes_are_strings(self):
        """  """
        self.assertTrue(type(self.review1.place_id), str)
        self.assertTrue(type(self.review1.user_id), str)
        self.assertTrue(type(self.review1.text), str)

    def test_save(self):
        """ """
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unnittest.main()
