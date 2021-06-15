/**
 * 
 * @author Rahul Rangarajan
 * @author Cameron King
 * @author Nick Jonas
 */
import java.util.concurrent.TimeUnit; 
public class CSC301Sorts {
	
	/**
	 * Runs and tests quicksort and mergesort
	 * @param args
	 * 
	 */
	public static void main(String[] args) {
		int[] a = randomArray(10000);
		long start = System.nanoTime();
		//quicksort(a, 0 , a.length -1);
		mergeSort(a, 0, a.length -1);
		long end = System.nanoTime();
		long timeElapsed = (end - start);
		System.out.println(timeElapsed);
		/*
		for(int x: a)
			System.out.print(x + ", ");
		*/
	}
	
	/**
	 * Creates a random array for use of sorts
	 * @param n : number of elements in array
	 * @return an array of size n
	 */
	
	public static int [] randomArray(int n) {
		int [] a = new int [n];
		for(int i = 0; i < a.length; i++) {
			a[i] = (int) (Math.random()*n);
		}
		return a;
	}
	/**
	 * Sorts a given array y using the sort known as quicksort
	 * @param a : array being used sorted by quicksort
	 * @param l : left of the array; also known as low 
	 * @param r : right of the array; also known as high
	 */
	public static void quicksort(int [] a, int l, int r) {
		int pivot = 0;
		if(l < r ) {
			int p = a[r];  
	        int i = (l-1);
	        for (int j=l; j<r; j++) { 
	            if (a[j] < p) { 
	                i++; 
	                swap(a, i, j);
	            } 
	        } 
	        swap(a, i+1, r);
	        pivot =i+1; 
		}
		else{
			return;
		}
		quicksort(a, l, pivot-1);
		quicksort(a, pivot+1, r);
	}
	/**
	 *  Swaps two elements in an array
	 * @param a : array being sorted by either quicksort or merge sort
	 * @param i : index of the first element being swapped
	 * @param j : index of second element being swapped
	 */
	public static void swap(int [] a, int i, int j) {
		int temp = a[i]; 
        a[i] = a[j]; 
        a[j] = temp; 
	}
	/**
	 * The main recursive algorithm in mergesort
	 * @param a : The array being sorted by mergesort
	 * @param l : left side of the array; also the low
	 * @param r : right side of the array; also the high
	 */
	public static void mergeSort(int [] a, int l , int r) {
		if(l < r) {
			// m is the mid point of array a
			int m = (l+r)/2;
			mergeSort(a, l, m);
			mergeSort(a, m+1, r);
			sort(a, l, m , r);
		}
	}
	/**
	 * The second part of merge sort which puts the array back together
	 * @param a : array being sorted
	 * @param l : left side of the array; also the low
	 * @param m : mid point of array 
	 * @param r : right side of the array; also the high
	 */
	public static void sort(int [] a, int l, int m , int r) {
		int [] L = new int [(m - l) + 1];
		int [] R = new int [ r- m];
		for(int i = 0; i < L.length; i++) {
			L[i] = a[l+i];
		}
		for(int i = 0; i < R.length; i++) {
			R[i] = a[m + i + 1];
		}
		
		int i = 0; 
		int j = 0;
		int k = l;
		
		while(i <= L.length-1 && j <= R.length-1) {
			if(L[i] < R[j]) {
				a[k] = L[i];
				i++;
			}
			else {
				a[k] = R[j];
				j++;
			}
			k++;
		}
		while(i < L.length) {
			a[k] = L[i];
			i++;
			k++;
		}
		while(j < R.length) {
			a[k] = R[j];
			j++;
			k++;
		}
	}
}
