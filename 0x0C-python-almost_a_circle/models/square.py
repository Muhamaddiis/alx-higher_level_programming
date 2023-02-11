#!/usr/bin/python3
"""creating a class square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a new square

        Args:
             size(int): The size of the new square.
             x (int): The x coordinate of the new square.
             y (int): The y coordinate of the new square.
             id (int): The identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getting the size of the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[square], ({}), {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.width)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
