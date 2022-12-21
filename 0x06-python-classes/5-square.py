#!/usr/bin/python3
"""
This module contains the Square class, which represents a square.
"""


class Square:
    """
    Class representing a square.

    The size of the square can be set and retrieved with proper validation.

    Attributes:
        __size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square to the console.

        If the size is 0, nothing is printed. Otherwise, the square
        is printed using the '#' character.
        """
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
