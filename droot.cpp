/* include files */
#include <math.h>
#include <iostream>

using namespace std;


// Global variables
long ops_count = 0L;


// Constant definitions
const long max_roots = 100000000L;
const double prec[10]= {\
	1.0,\
	0.1,\
	0.01,\
 	0.001,\
	0.0001, \
	0.00001, \
	0.000001, \
	0.0000001, \
	0.00000001, \
	0.000000001 };


double roots[max_roots];

double root(double val, int places) {
    double p2;
    double r=val / 2.0;
    double diff;

    // Calculate precision check
    if  (places <10)
	p2 = prec[places];
    else
    {
	p2=0.1;
	for (int i=1; i<places; i++ ) 
	    p2 *= 0.1;
    } //if else

    //Main root calculation
    do {
	diff=(r*r-val)/(2*r);
	r-=diff;
	ops_count += 1L;
    } while (diff>=p2);
    return r;
} // root

int main(int argc, char *arv[])
{
    for (long l=0L; l<max_roots;l++) 
    {
	roots[l] = root((double)(l+1L),3);
    } // for

    cout << "Ops Cout"<<ops_count<<'\n';

    return (0);

} //main
	
