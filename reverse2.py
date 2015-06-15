#!/usr/bin/python


orig = raw_input("Type a phrease: ") 

def reverse(str):
	i=1
	rest = ""
	while i <= len(str):
		rest = rest + str[-i]
                i=i+1
	return rest


rest = reverse(orig)
if orig[:len(orig)/2+len(orig)%2]==rest[:len(rest)/2+len(rest)%2]:
    print "**palindrome**"
else:
    print "reverse= ", rest
