package arrays;
import java.util.ArrayList;
public class List {

	public static void main(String[] args) {
		
		ArrayList<String> color = new ArrayList<String>();
		
		color.add("Black");
		color.add("Gray");
		color.add("White");
		color.add("Purple");
		
		//color.set(0, "Brown");
		//color.remove(3);
		//color.clear();
		
		for(int i=0; i<color.size(); i++) {
			System.out.println(color.get(i));
		}

	}

}
