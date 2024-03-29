#!/usr/bin/python3
"""
Class that defines a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a square
    """

    def __init__(self, size):
        """
        Instantiation with size: def __init__(self, size):
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Public instance method: def area(self):
        that returns the area of the square
        """

        return self.__size * self.__size
