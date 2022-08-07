#!/usr/bin/python3
"""
contains a class inheriting from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """attributes of Review classs"""
    place_id = ""
    user_id = ""
    text = ""
