#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    return(my_string.translate({ord(letter): None for letter in 'Cc'}))
