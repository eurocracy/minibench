// Include files
#include <iostream>
#include <stdlib.h>

using namespace std;

//Constants
const long MaxInteger = 100000000;

//Global variables
bool e[MaxInteger];

class Sieve
{
    
    public:static bool dgsieve(long max)
    {

	e[1] = true;
	for (int i = 2; i <= max; i++)
	{
	    e[i] = true;
	} //for

	for(int j = 2; j < max; j++)
	{
	    if (e[j])
	    {
		for (int p=j+j; p<=max; p+=j)
		{
		    e[p] = false;
		} // for
	    } // if
	} // for
	return e[max];
    } // dgsieve 
};//Sieve

    int main(int argc, char *argv[])
    {
	long max;

	if (argc != 2)
	{
	    std::cout << "Usage Sieve <max prime>\n";
	} 
	else
	{
	    max = atol(argv[1]);
	    if ( Sieve::dgsieve(max)  )
		std::cout << "Is Prime\n";
	} // if else
    } // main

