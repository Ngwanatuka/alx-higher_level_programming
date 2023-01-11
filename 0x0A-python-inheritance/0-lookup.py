#!/usr/bin/pyhton3

""" Define an object attribute lookup function."""


def lookup(obj):
    """
    retunr a list of the available attributes and 
    methods of an object
    """

    return dir(obj)
