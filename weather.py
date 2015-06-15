#!/usr/bin/python

sum = ncold = 0

for i in range(0,7):
    temp=input()
    sum = sum + temp
    if temp < 0:
        ncold += 1

avt = sum/7.0

print avt
print ncold


