#!/usr/bin/python3
"""Class square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update  square """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.height = value
                    self.width = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "y":
                    self.y = value
                if key == "x":
                    self.x = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width, self.height)

    def to_dictionary(self):
        """Return dictionary representation of square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
