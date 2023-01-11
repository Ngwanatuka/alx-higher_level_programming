#!/usr/bin/python3

"""A class that inherits from the built-in 'list' class"""


class MyList(list):
    """ Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Prints a list in sorted ascending order"""
        print(sorted(self))
