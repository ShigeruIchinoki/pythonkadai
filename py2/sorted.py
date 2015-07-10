#!/usr/bin/python
li=["gutenberg","a","all","alice","project"]
def foo(s):
    return s[-1]
def cmp_len(a, b):
    return cmp(len(a), len(b))
print sorted(li, cmp=cmp_len)
print sorted(li, key=len)
