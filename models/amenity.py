#!/usr/bin/python3
"""Defines the Amenity class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the Amenity class.
    Attributes:
        name (str): The amenity name.
    """
    name = ""
