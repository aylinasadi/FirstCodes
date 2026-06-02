package arrays;

public class Main3 {

	public static void main(String[] args) {
		
		int[][] numbers = new int[3][3];
		
		numbers[0][0] = 120;
		numbers[0][1] = 121;
		numbers[0][2] = 122;
		numbers[1][0] = 123;
		numbers[1][1] = 124;
		numbers[1][2] = 125;
		numbers[2][0] = 126;
		numbers[2][1] = 127;
		numbers[2][2] = 128;
		
		for(int i=0; i<numbers.length; i++) {
			System.out.println();
			
			for(int j=0; j<numbers[i].length; j++) {
				System.out.print(numbers[i][j]+" ");
			}
			
		}
		
		/*int[][] numbers = {
		 *                    {120,121,122},
		 *                    {123,124,125},
		 *                    {126,127,128}
		 *                  };
		 *
		 *for(int i=0; i<numbers.length; i++) {
			System.out.println();
			
			for(int j=0; j<numbers[i].length; j++) {
				System.out.print(numbers[i][j]+" ");
			}
			
		}
		 */

	}

}
