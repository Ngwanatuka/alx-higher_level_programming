#!/usr/bin/python3
"""Module containing a dummy adder function for testing"""


def add_integer(a, b=98):
    """
    Add two integers.
    
    Parameters:
    a (int or float): The first integer to be added.
    b (int or float, optional): The second integer to be added. Defaults to 98 if not given.
    
    Raises:
    TypeError: If `a` or `b` are not integers or floats.
    
    Returns:
    int: The sum of `a` and `b`.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or a float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
