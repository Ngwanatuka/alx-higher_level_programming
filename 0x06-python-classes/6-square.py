#!/usr/bin/python3
"""
This module contains the Square class, which represents a square.
"""


class Square:
    """
    Class representing a square.

    The size and position of the square can be set and retrieved with proper validation.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square, represented as a tuple of 2 integers.

    Raises:
        TypeError: If the size is not an integer, or if the position is not a tuple of 2 positive integers.
        ValueError: If the size is less than 0, or if the position is not a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square, represented as a tuple of 2 integers. Defaults to (0, 0).

        Raises:
            TypeError: If the size is not an integer, or if the position is not a tuple of 2 positive integers.
            ValueError: If the size is less than 0, or if the position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square, represented as a tuple of 2 integers.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The
