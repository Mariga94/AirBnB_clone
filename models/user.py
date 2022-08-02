#!usr/bin/python3
"""
A class user that inherits from BaseModel
"""
from ast import Pass
import email
from models.base_model import BaseModel
class User(BaseModel):
    """class attributes of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
