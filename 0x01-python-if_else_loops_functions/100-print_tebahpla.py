#!/usr/bin/python3
for j in range(ord('z'), ord('a') -1, -1):
    if j % 2 == 0:
        diff = 0
    else:
        diff = 32
        print('{}'.format(chr(j - diff)), end='')
