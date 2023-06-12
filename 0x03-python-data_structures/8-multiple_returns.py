#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        first_c = sentence[0]
    else:
        first_c = None
        return (len(sentence), first_c)
