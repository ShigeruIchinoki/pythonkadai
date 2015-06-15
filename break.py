#!/usr/bin/python

nums=[100,120,34,25,50,75,205]

for n in nums:
  if n >=100:
    continue
  print n

count = 0
while True:
    count = count +1
    print count 
    if count > 10:
        break

count =0
while True:
  count = count +1
  print count
  if count <10:
    continue
  break


