#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    if not my_list:
        return my_list
    my_set = set(my_list)
    return sum(my_set)
