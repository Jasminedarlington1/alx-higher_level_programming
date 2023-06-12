#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listc = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return (listc)
    else:
        listc[idx] = element
        return (listc)
