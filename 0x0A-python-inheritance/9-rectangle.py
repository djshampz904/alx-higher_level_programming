#!/usr/bin/python3
""" 
Class that defines a rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    __width = 0
    __height = 0
    
    def __init__(self, width, height):
        """ 
        Instantiation with width and height: def __init__(self, width, height):
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """ 
        Public instance method: def area(self): that returns the area of the rectangle
        """
        return self.__width * self.__height
    
    def __str__(self):
        """ 
        Return the following rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def __repr__(self):
        """ 
        Return the following rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
