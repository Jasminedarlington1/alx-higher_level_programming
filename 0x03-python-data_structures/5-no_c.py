#!/usr/bin/python3
def no_c(my_string):
    strr = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            strr += i
            return (strr)
