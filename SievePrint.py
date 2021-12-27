#!/usr/bin/python3
import sys
import math
from bitarray import bitarray


   
def dgsieve(max):
#    print(max)
    e = bitarray(max)
    e.setall(True)
    print(2)
 
    for j in range(3,int(max),2):
        if (e[j]):
            print(j)
            for p in range(j+j,max,j):
                e[p] = False

#Main code block
def main():
#    print ("Damian's Sieve of Eratosthenes")
    l = len(sys.argv)
#    print(l)
    if (l!=2):
        print("Usage: Sieve.py <number>")
        quit()
    n = int(sys.argv[1])
    dgsieve(n)
 #   print("End")

#Now call the main function
main()
