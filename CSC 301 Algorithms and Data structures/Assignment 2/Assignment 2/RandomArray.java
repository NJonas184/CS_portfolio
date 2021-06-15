
/**
 * Write a description of class RandomArray here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Random;
public class RandomArray
{
    public static int[] randomArray(int n){
        Random rng = new Random();
        int[] array = new int[n];
        for(int i = 0; i<n; i++){
            array[i] = rng.nextInt(100);
        }

        return array;
    }

    public static void main(String args[]){
        int[] a = randomArray(10);
        for(int i = 0; i<a.length; i++){
            System.out.println(a[i]);
        }
    }
}
