#!/usr/bin/python3
""" 
Class that defines a rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ 
    Class that defines a rectangle
    """
    __width = 0
    __height = 0
    
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
