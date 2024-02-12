#!/usr/bin/python3
""" Base class """


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base class """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset(cls):
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON string representation of list_dictionaries """
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))
