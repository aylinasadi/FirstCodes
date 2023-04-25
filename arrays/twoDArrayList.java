package arrays;
import java.util.*;
public class twoDArrayList {

	public static void main(String[] args) {
		ArrayList<ArrayList<String>> MyFavs = new ArrayList();
		
		
		ArrayList<String> colors = new ArrayList();
		colors.add("black");
		colors.add("Purple");
		
		ArrayList<String> foods = new ArrayList();
		foods.add("caesar salad");
		foods.add("kabab torsh");
		
		ArrayList<String> subjects = new ArrayList();
		subjects.add("forensic anthropology");
		subjects.add("comp sci");
		subjects.add("cog sci");
		
		
		MyFavs.add(colors);
		MyFavs.add(foods);
		MyFavs.add(subjects);
		
		
		
		//System.out.println(subjects);
		//System.out.println(MyFavs.get(0));
		System.out.println(MyFavs.get(1).get(0));
		//System.out.println(MyFavs);
		
		

	}

}
