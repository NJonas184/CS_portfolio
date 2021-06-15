import java.util.Scanner;
/**
 * Prints out all of the permutations of length k of a given string of length k
 * @author Cameron King
 * @author Nick Jonas
 * @author Rahul Rangarajan
 */
public class Permutations {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Please enter the String that you would like all the permutations for");
		String strInput = sc.nextLine();
		char[] charElements = strInput.toCharArray();
		permutation(charElements, 0, charElements.length-1);
	}
	/**
	 * Recursive method that prints out all of the permutations of a given string
	 * @param charElements : character array 
	 * @param intLeft : the first value in the array. Changes based on which element is currently set to be first
	 * @param intRight : the length of the array or the position of the last element in the array
	 */
	public static void permutation(char[] charElements, int intLeft, int intRight) {
		if(intLeft == intRight) 
			System.out.println(charElements.toString());
		else {
			for (int i = intLeft; i <= intRight; i++) {
				swap(charElements, intLeft, i);
				permutation(charElements, intLeft+1, intRight);
				swap(charElements, intLeft, i);
			}
		}
	}
	/**
	 * Swaps the values of positions i and j 
	 * @param charElements : array of char that contains the characters in the String 
	 * @param intIndexi : index i or the position of the first value being swapped
	 * @param intIndexj : index j or the position of the second value being swapped
	 */
	public static void swap(char[] charElements, int intIndexi, int intIndexj) {
		char intTemp = charElements[intIndexi];
		charElements[intIndexi] = charElements[intIndexj];
		charElements[intIndexj] = intTemp;
	}
}
