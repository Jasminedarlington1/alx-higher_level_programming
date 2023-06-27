#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing a new class"""

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
        """Area of square
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
