#!/usr/bin/python3
"""
Unittest for Place model class
"""
from models.base_model import BaseModel
import unittest
import os
from models.state import State


class test_State(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ """
        cls.state1 = State()
        cls.state1.name = "Kism"

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """ """
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_doc(self):
        """ """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """ """
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        """  """
        self.assertTrue(type(self.state1.name), str)

    def test_save(self):
        """ """
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unnittest.main()
