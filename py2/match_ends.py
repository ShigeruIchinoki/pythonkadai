#!/usr/bin/python

def match_ends(li):
    n = 0
    for i in li:
        if len(i) >= 2 and i[0] == i[-1]:
            n = n + 1
        return n


print match_ends(['ba', 'xyz', 'aa', 'x', 'bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])
     


