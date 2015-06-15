#!/usr/bin/python


def fb(n):
    str = ""
    if n%5 == 0:
        str = str + "Buzz"
    if n%3 == 0:
        str = "Fizz" + str
    return str

i = 1
while i <=20:
    print i, fb(i)
    i = i + 1

