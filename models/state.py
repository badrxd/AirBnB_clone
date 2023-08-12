#!/usr/bin/python3
"""Defines the State class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the State class.
    Attributes:
        name (str): The state name.
    """
    name = ""
