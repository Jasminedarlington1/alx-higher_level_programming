#!/usr/bin/python3
"""Creates a square class"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """
        Initializing a new class
        """

        self.__size = size

    @property
    def size(self):
        """Getter"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Area square
        """

        return (self.__size)**2
