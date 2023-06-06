#!/usr/bin/python3
for letter in range(0, 10):
    for l in range(0, 10):
        if letter >= l:
            continue
        elif letter >= 8 and l >= 9:
            print("{:d}{:d}".format(letter, l))
        else:
            print("{:d}{:d}, ".format(letter, l), end='')
