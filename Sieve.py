#!/usr/bin/python3
import sys #needed for command line arguments
from bitarray import bitarray

# Global variable to hold boolean array as a bitarray
e = bitarray()
   
def dgsieve(max):
    global e
    print(max)
    #Check ifit's an even value
    if max&1 != 1 :
        return(False)
    for i in range(0,max+1):
        e.append(True)
    for j in range(3,max,2):
        if (e[j]):
            for p in range(j+j,max+1,j):
                e[p] = False
    return e[max]

#Main code block
def main():
    print ("Damian's Sieve of Eratosthenes")
    l = len(sys.argv)
    print(l)
    if (l!=2):
        print("Usage: Sieve2.py <number>")
        quit()
    n = int(sys.argv[1])
    if (dgsieve(n)):
            print("Is Prime")
    print("End")

main()
