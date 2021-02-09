#!/usr/bin/python3
import sys
from bitarray import bitarray


   
def dgsieve(max):
    print(max)
    #Check ifit's an even value
    if max&1 != 1 :
        return(False)
    e = bitarray(max+1)
    e.setall(True)
 
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
        print("Usage: Sieve.py <number>")
        quit()
    n = int(sys.argv[1])
    if (dgsieve(n)):
            print("Is Prime")
    print("End")

#Now call the main function
main()
