#!/bin/usr/python3
""" A Module that contains class Rectangle,
inherits
"""
from models.base import Base

class Rectangle(Base):
    """ class Rectangle """
    def __init__(self, width, height, x=0, y=0):

    """
    Initializes a new Rectangle instance

    Arg:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int, optional): The x-coordinate of the rectangle.
    Default to 0.
    y (int, optional): The y-coordinate of the rectangle.
    Defaults to 0.
    """

        super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
