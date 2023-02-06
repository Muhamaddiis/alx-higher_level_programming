#!/usr/bin
"""creating class list"""


class MyList(list):
    """inherits from List"""
    def print_sorted(self):
        """sorts list"""
        print(sorted(self))
