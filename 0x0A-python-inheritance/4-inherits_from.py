#!/usr/bin/python3
"""
a function that returns True if the object is
an instance of a class that inherited
(directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    returns:
            If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """

    return type(obj) != a_class and isinstance(obj, a_class)
