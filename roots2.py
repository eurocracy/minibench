#!/usr/bin/python3
import math

MaxRoots = 10000000
roots = []

#Main program
for i in range (0,MaxRoots+1):
    roots += [math.sqrt(i+1)]
#    print("Root: %d:%8.2f" % (i,roots[i]))
	
