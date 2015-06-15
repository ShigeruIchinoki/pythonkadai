#!/usr/bin/python

def front_back(a, b):
    awaru = len(a)/2
    ajouyo = len(a)%2
   
    bwaru = len(b)/2
    bjouyo = len(b)%2
 
    ret = a[:awaru+ajouyo]+b[:bwaru+bjouyo]+a[awaru:]+b[bwaru:]

    return ret

print front_back("abcde", "xy")
