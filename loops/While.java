package loops;
import java.util.Scanner;
public class While {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
	    String name = "";
		
		while(name.isBlank()) {
			System.out.print("What is your name? ");
			name = scanner.nextLine();
		}
		System.out.println("Hello "+name);
		
		/*do{
			*System.out.print("What is your name? ");
			*name = scanner.nextLine();
		*}while(name.isBlank());
		*
		*System.out.println("Hello "+name);
		*/
		scanner.close();

	}

}
