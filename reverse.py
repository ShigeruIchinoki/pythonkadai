#!/usr/bin/python
def reverse(str):
	i=1
	rest = ""
	while i <= len(str):
		rest = rest + str[-i]
                i=i+1
	return rest


orig = "good moning"
rest = reverse(orig)
print rest
