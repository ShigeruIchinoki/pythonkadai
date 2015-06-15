#!/usr/bin/python

def first_last(s):
    if len(s) < 2:
       ret = ""
    else:
       ret = s[:2] + s[-2:]
    return ret

print first_last("Sprint")

print first_last("int")
print first_last("Sprint")
print first_last("t")
