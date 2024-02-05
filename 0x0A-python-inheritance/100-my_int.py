class MyInt(int):
    """
    A class that inherits from int and inverts the == and != operators

    >>> my_int = MyInt(3)
    >>> my_int == 3
    False
    >>> my_int != 3
    True
    >>> my_int == 4
    True
    >>> my_int != 4
    False
    """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
