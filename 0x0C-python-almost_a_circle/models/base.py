#!/usr/bin/pyhton3
""" Model that contains class Base """
import json
import csv
import os.path


class   Base:
    """ Calss Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
