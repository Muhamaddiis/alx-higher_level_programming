#!/usr/bin/python3
"""create a function"""


def text_indentation(text):
    """a function that prints a text with 2 new
    lines after each of these characters: ., ? and :

    args:
    @text:
        text (string): The text to print.
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
