#!/usr/bin/python3
""" function that reads a text file(utf8) and prints it to stdout"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as myFile:
        read_file = myFile.read()
        print(read_file, end="")
