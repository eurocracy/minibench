#!/usr/bin/python3

MaxRoots = 10000000

prec = [ 1.0,
	0.1,
	0.01,
 	0.001,
	0.0001, 
	0.00001, 
	0.000001, 
	0.0000001, 
	0.00000001, 
	0.000000001 ]

roots = [0]

def root(val,places=2):
    if (places <10):
        p2 = prec[places]
    else:
        p2 = 0.1
        for i in range(0,places):
            p2 *= 0.1

    r = val/2.0
    while True:
        diff =(r*r-val)/(r+r)
        r -= diff
        if diff <p2:
            break
    return r

#Main program
for i in range (0,MaxRoots):
    roots += [root(i+1)]
#    print("Root: %d:%8.2f" % (i,roots[i]))
	
