#!/usr/bin/python3
def no_c(my_string):
    t = ''
    for a in my_string:
        if a != 'c' and a != 'C':
            t += a
            return (t)
