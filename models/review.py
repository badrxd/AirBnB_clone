#!/usr/bin/python3
"""Defines the Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Review class.
    Attributes:
        place_id (str): The id of the place.
        user_id (str): The id of the user.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
