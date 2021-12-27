#!/usr/bin/python3
import math #needed for sqrt
import sys #needed for command line arguments

def factor(n):
    #First check it isn't even
    if (int(n)&1) == 0:
        return 2
    else:
        #We add +2 to ensure we check exact integer square roots
        r = int(math.sqrt(n))+2
        for i in range(3,r,2):
            if (n % i) == 0:
                return i
        return n

def all_factors(n):
    factors=[]
    r = n
    while (r !=1):
        t = factor(r)
        factors += [t]
   #     print(t)
        r = int(r/t)
    return factors

#Main code block
def main():
    print ("Damian's prime factorisation")
    l = len(sys.argv)
    if (l!=2):
        print("Usage: Sieve2.py <number>")
        quit()
    n = int(sys.argv[1])
#    print(factor(n))
    f = all_factors(n)
    print(f)

main()
