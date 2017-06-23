public class Sieve {
    
    private static void dgsieve(int max)
    {
	boolean[] e;

	e = new boolean[max];
	e[1] = true;
	for (int i = 2; i < max; i++)
	{
	    e[i] = true;
	} //for

	for(int j = 2; j < max; j++)
	{
	    if (e[j])
	    {
		for (int p = 2; (p*j) < max; p++)
		{
		    e[p *j] = false;
		} // for
	    } // if
	} // for
    } // dgsieve

    public static void main(String[] args)
    {
	long max;

	if (args.length != 1)
	{
	    System.out.println("Usage Sieve <max prime>");
	} else {
	    max = Long.parseLong(args[0], 10); 	    
	    dgsieve((int)max);
	} // if else
    } // main
} // Sieve`
