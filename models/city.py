#!/usr/bin/python3
"""
contains a class city inheriting from Basemodel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City attributes"""
    state_id = ""
    name = ""
