#!/usr/bin/python3
"""creating the square"""


class Square():
    """creating the init function"""
    def __init__(self, size=0):
        """nitializing the size of the attribute
        and setting it to private
        Args:
        size(int): the size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.__size * self.__size
