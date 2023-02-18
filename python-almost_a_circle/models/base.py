#!/usr/bin/python3
# Alex Nuñez <5694@holbertonstudents.com>
"""Define a class Base."""
import json


class Base:
    """Create a class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dic."""
        if list_dictionaries == [] or list_dictionaries is None:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string of list object to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string."""
        if json_string is None or json_string == "[]":
            return([])
        else:
            return(json.loads(json_string))
