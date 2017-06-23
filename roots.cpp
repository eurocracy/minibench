/* include files */
#include <math.h>

// Constant definitions
const long max_roots = 10000000L;
const float prec[10]= {\
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


float roots[max_roots];

float root(float val, int places) {
    float p2;
    float r=val / 2.0;
    float diff;

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
    } while (diff>=p2);
    return r;
} // root

int main(int argc, char *arv[])
{
    for (long l=0L; l<max_roots;l++)
	roots[l] = root((float)(l+1L),3);

    return (0);

} //main
	
