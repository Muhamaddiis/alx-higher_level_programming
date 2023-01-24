#!/usr/bin/python3
class Square():
    """Defining the square"""
    def __init__(self, size):
        """initializing the size attribute and making it private

        Args:
            size: the size of the square
        """
        self.__size = size
