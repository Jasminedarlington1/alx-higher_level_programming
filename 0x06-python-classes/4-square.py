#!/usr/bin/python3


class Square:
    """Square class"""

    def __init__(self, size=0):
        """
        Initializing the square size
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Getter"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value)not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Area square
        """

        return (self.__size)**2
