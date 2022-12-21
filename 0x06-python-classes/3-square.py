#!/usr/bin/python3
"""
This module contains the Square class, which represents a square.
"""


class Square:
    """
    Class representing a square.

    The size of the square is initialized with proper validation.

    Attributes:
        __size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
