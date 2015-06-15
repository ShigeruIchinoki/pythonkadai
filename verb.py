#!/usr/bin/python

def verb_ing(s):
    if len(s)>3 and s[-3:]=="ing":
        ret = s + "ly"
    elif len(s)>3:
        ret = s + "ing"
    else:
        ret = s
    return ret


print verb_ing("intttttt")
print verb_ing("in")
print verb_ing("inting")
print verb_ing("t")
print verb_ing("int")
