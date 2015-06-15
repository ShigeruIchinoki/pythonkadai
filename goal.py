#!/usr/bin/python

def goal(count):
    if count <9:
        ret = "Number of goals: " + str(count)
    else:
       ret = "manyi"
    return ret

print goal(4)
print goal(9)
print goal(99)
print goal(99)
