import java.math.BigInteger;

public class Mersenne {

    
    private static void Mcalc(int power)
    {
	BigInteger one = new BigInteger("1");
	BigInteger m = one.shiftLeft(power);
	BigInteger p = m.subtract(one);
	System.out.println("M(" +power +"): " + p);
    } // Mcalc

    public static void main(String[] args)
    {
	long power;

	if (args.length != 1)
	{
	    System.out.println("Usage Mersenne <power of two>");
	} else {
	    power=Long.parseLong(args[0], 10); 	    
	    Mcalc( (int) power);

	} // if else
    } // main
} // Mersenne
