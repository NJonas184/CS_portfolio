import java.util.Scanner;
public class Permutations {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Please enter the String that you would like all the permutations for");
		String strInput = sc.nextLine();
		char[] charElements = strInput.toCharArray();
		permute(charElements, 0, charElements.length-1);
	}
	
	public static void permute(char[] charElements, int intLeft, int intRight) {
		if(intLeft == intRight) 
			printArray(charElements);
		else {
			for (int i = intLeft; i <= intRight; i++) {
				swap(charElements, intLeft, i);
				permute(charElements, intLeft+1, intRight);
				swap(charElements, intLeft, i);
			}
		}
	}
	
	public static void printArray(char[] charElements) {
		System.out.println();
		for(char x: charElements)
			System.out.print(x);
	}
	
	public static void swap(char[] charElements, int intIndex0, int intIndex1) {
		char intTemp = charElements[intIndex0];
		charElements[intIndex0] = charElements[intIndex1];
		charElements[intIndex1] = intTemp;
	}
}
