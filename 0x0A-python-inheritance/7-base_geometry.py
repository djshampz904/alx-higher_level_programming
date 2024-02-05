#!/bin/usr/python3
class BaseGeometry:
    
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value): that validates value
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
