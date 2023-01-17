#!/bin/usr/python3
""" Model that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """ A class that represents a rectangle and inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inititialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle.
            Defaults to 0.
            x (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The id of the rectangle.
            Defaults to None.

        Raises:
            TypeError: if width, height, x, or y is not an integer.
            x or y is under 0.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heihgt must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of a rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the redtangle.


        Returns:
            int: Hte area of a rectangle.
        """

        return self.width * self.height

    def display(self):
        """
        Prints the ractange represented by the # character in stdout.
        """

        for i in range(self.height):
            print("#" * self.width)
        """Print the ractangle with the character # in stdout,
        taking care of x and y."""
        print("\n" * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle]({self.id})" "{self.x}/{self.y}" "-"
    "{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ update method """
        args_and_kwargs = dict(zip(['id', 'width', 'height', 'x', 'y'], args))
        args_and_kwargs.update(kwargs)
        for key, value in args_and_kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
