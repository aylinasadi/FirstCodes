package logical_operators;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("What is today's temperature?");
		int temp = scanner.nextInt();
		
		if(temp>30) {
			System.out.println("It is hot outside");
		}
		else if(temp>=20 && temp<=30) {
			System.out.println("It is warm outside");
		}
		else if(temp>=0 && temp<20) {
			System.out.println("It is cold outside");
		}
		else {
			System.out.println("It is freezing outside");
		}
		scanner.close();

	}

}
