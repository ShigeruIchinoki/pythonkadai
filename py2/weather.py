#!/usr/bin/python

sum = ncold = 0

for i in range(0, 7):
    tenp = input()
    sum = sum + tenp
    if tenp < 0:
       ncold += 1


avt = sum / 7.0

print avt
print ncold


