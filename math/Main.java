package math;

public class Main {

	public static void main(String[] args) {
		
		double x = 6.22;
		double y = -3;
		
		double z = Math.max(x, y);
		System.out.println(z);
		
		double a = Math.min(x, y);
		System.out.println(a);
		System.out.println(Math.abs(a));
		
		double b = Math.sqrt(x);
		System.out.println(b);
		System.out.println(Math.round(b));
		System.out.println(Math.ceil(b));
		
		double c = 5.67;
		System.out.println(Math.floor(c));
		
	}

}
