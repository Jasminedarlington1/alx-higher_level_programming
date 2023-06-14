#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (list(map(lambda new_element: new_element if new_element != search else replace, my_list)))
