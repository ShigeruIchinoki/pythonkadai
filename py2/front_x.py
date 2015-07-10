#!/usr/bin/python

def front_x(li):
    all = []
    l1 = []
    l2 = []
    for s in li:
      if s[0]=="x":
        l1.append(s)
      else:
        l2.append(s)
    all = sorted(l1) + sorted(l2)
    return all


print front_x(['ba', 'xyz', 'aa', 'x', 'bbb'])
print front_x(['a', 'x', 'xy', 'xyx', 'xx'])
print front_x(['aaa', 'be', 'abc', 'hello'])
     


