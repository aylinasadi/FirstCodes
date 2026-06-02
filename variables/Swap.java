package variables;

public class Swap {

	public static void main(String[] args) {
		
		String x = "water";
		String y = "soda";
		String temp =null;  //can also do String temp;
		
		temp = x;
		x=y;
		y=temp;
		
		System.out.println("x: "+x);
		System.out.println("y: "+y);

	}

}
