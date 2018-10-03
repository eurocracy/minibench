#!/usr/bin/pypy
import sys


e = []
   
def dgsieve(max):
    print(max)
    for i in range(0,max+1):
	e.append(True)

    for j in range(2,max):
	if (e[j]):
	   for p in range(j+j,max+1,j):
		e[p] = False
        
    return e[max] 

#Main code block
def main():
    print ("Damian's Sieve of Eratosthenes")
    l = len(sys.argv)
    print(l)
    if (l==2):
	max = int(sys.argv[1])

	if (dgsieve(max)):
	    print("Is Prime")
    else:
	print("Usage: Sieve <prime>")
    print("End")

main()
