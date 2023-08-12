#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place


print("-- Create a new place --")
my_place = Place()
my_place.number_rooms = 15
my_place.latitude = 13.5
my_place.save()
print(my_place)

