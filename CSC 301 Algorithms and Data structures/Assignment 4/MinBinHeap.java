
/**
 * BinHeap is a class simulating a Heap with Min Heap capabilities.
 *
 * @author Cameron King, Nick Jonas, Rahul Rangarajan
 */
import java.io.IOException;
public class MinBinHeap {
    private int heapSize;
    private int[] heapArray;
    //Constructor initializing array
    public MinBinHeap(){
        heapSize = 10;
        heapArray = new int[10];
    }
        public MinBinHeap(int size){
        heapSize = size;
        heapArray = new int[size];
    }
    //function to return parent of position i on the array
        public int parent(int i){
            return ((i/2)-1);
    }
    //function to return left child of position i on the array
        public int left(int i){
            return (i*2)+1;
    }
    //function to return right childe of position i on the array
        public int right(int i){
            return (i*2)+2;
    }
    //function to organise "nodes" on the array into proper min heap formation
    //@param i signifies the position of the parent node being compared
        public void Min_heapify(int i){
            int l = left(i);
            int r = right(i);
            int smallest = i;
            if((l < heapSize) && (heapArray[l] < heapArray[i])){
                smallest = l;
            }
            if((r < heapSize) && (heapArray[r] < heapArray[smallest])){
                smallest = r;
            }
            if(smallest != i){
                int temp = heapArray[i];
                heapArray[i] = heapArray[smallest];
                heapArray[smallest] = temp;
                Min_heapify(smallest);
            }
        }
        //function to turn an entire array into a minimum heap
        public void BuildMinHeap(){
            for(int i = (heapSize/2)-1; i >= 0; i--){
                Min_heapify(i);
            }
        }
        //function that takes heapArray and resizes it
        //@param newSize is the required newSize of the heapArray
        public void resize(int newSize){
            int temp[] = new int[newSize];
            for(int i = 0; i<heapSize; i++){
                temp[i] = heapArray[i];
            }
            heapArray = new int[newSize];
            for(int i = 0; i < heapArray.length; i++){
                heapArray[i] = temp[i];
            }
            
        }
        //function that adds a newValue to the heap
        //@param newValue is the value stored in the "node"
        public void addElement(int newValue){
            if(heapSize == heapArray.length){
                resize(heapSize*2);
            }
            else if(heapSize == (heapArray.length/4)){
                resize(heapArray.length/2);
            }
            heapArray[heapSize] = newValue;
            heapSize++;
            int p = parent(heapSize-1);
            int index = heapSize-1;
                while(p>=0 && heapArray[index] > heapArray[p]){
                    int temp = heapArray[index];
                    heapArray[index] = heapArray[p];
                    heapArray[p] = temp;
                    index = p;
                    p = parent(index);
                }
        }
        /*
         * function to remove the smallest number from the heap and returns it
         * and then maintains its min heap form
         */
        
        public int ExtractMin(){
            int min = heapArray[0];
            heapArray[0] = heapArray[heapSize-1];
            heapSize--;
            Min_heapify(0);
            return min;
        }
        /*
         * private search function for public search function below
         * @param key is the value being searched for
         * @param index is the current index being compared
         */
        private int search(int key, int index){
            if(index < heapSize){
                if(key == heapArray[index]){
                    return index;
                }
                int l = search(key, left(index));
                if(l != -1){
                    return l;
                }
                int r = search(key, right(index));
                if(r != -1){
                    return r;
                }
            }
            return -1;
        }
        /*
         * function that searches the heap for a key using the private Search
         * function
         * @param key is the value being searched for
         */
        public void search(int key) throws IOException{
             int search = search(key, 0);
             if(search == -1){
                 throw new IOException("KEY DOES NOT EXIST IN HEAP");
                }
                else{
                System.out.println(search);
                }
             
        }
    
    public static void main(String args[]) throws IOException {
        
        MinBinHeap BH = new MinBinHeap(11);
        BH.heapArray[0] =11;
        BH.heapArray[1] =10;
        BH.heapArray[2] =9;
        BH.heapArray[3] =8;
        BH.heapArray[4] =7;
        BH.heapArray[5] =6;
        BH.heapArray[6] =5;
        BH.heapArray[7] =4;
        BH.heapArray[8] =3;
        BH.heapArray[9] =2;
        BH.heapArray[10] = 1;
        BH.BuildMinHeap();
        
        for(int i = 0; i<BH.heapSize; i++){
            System.out.print(BH.heapArray[i] + " ");
        }
    }
        
}

