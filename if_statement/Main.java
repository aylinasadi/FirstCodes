package if_statement;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("How old are you?");
		int age = scanner.nextInt();
		
		
		if(age>=20) {
			System.out.println("You are an adult!");
		}
		
		else if(age>=13) {
			System.out.println("You are a teenager!");
		}
		
		else if(age>=4) {
			System.out.println("You are a kid!");
		}
		
		else {
		System.out.println("You are a toddler!");
		}
			
		scanner.close();

	}

}
