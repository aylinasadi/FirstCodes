package logical_operators;
import java.util.Scanner;
public class Main3 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("If you want to exit the game, Press E or e and if not, Press any key");
		String answer = scanner.next();
		
		if(!answer.equals("e") && !answer.equals("E")) {
			System.out.println("You are still playing");
		}
		else {
			System.out.println("You closed the game");
		}
		scanner.close();
	}

}
