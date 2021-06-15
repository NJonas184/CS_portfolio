
/**
 * Write a description of class TimeElapsed here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.concurrent.TimeUnit; // requires exceptions

public class TimeElapsed
{
   public static void main(String args[]) throws InterruptedException{
   long start = System.nanoTime(); //creates start time
   
   TimeUnit.SECONDS.sleep(3); //stalls for 3 seconds
   
   long end = System.nanoTime(); //creates end time
   
   long timeElapsed = end - start;
   
   System.out.println("nanoseconds elapsed: " + timeElapsed); 
   //will compute to a little over 3 seconds in nanoseconds
   
    }
}
