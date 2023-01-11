#!/usr/bin/python3

""" Implementation of a function that can read a text file(UTF8) """

def read_file(filename=""):
	""" Reads a text file and prints its content to stdout."""
	with open(filename, 'r', encoding='utf-8') as file:
		print(file.read(), end="")
