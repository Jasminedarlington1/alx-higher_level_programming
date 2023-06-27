#!/usr/bin/python3
"""Creates a square"""


class Square:
    """Not an empty square"""

    def __init__(self, size=0):

        """Initializing the class square with size attribute"""
        self.__size = size

        if type(size) is not a int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueErrore("size must be >= 0")
