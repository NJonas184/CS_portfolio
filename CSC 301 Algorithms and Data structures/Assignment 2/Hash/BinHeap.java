
/**
 * BinHeap is a class simulating a Heap with Max Heap capabilities.
 *
 * @author Cameron King, Nick Jonas, Rahul Rangarajan
 */
import java.io.IOException;
public class BinHeap {
    private int heapSize;
    private int[] heapArray;
    //Constructor initializing array
    public BinHeap(){
        heapSize = 10;
        heapArray = new int[10];
    }
        public BinHeap(int size){
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
    //function to organise "nodes" on the array into proper max heap formation
    //@param i signifies the position of the parent node being compared
        public void Max_heapify(int i){
            int l = left(i);
            int r = right(i);
            int largest = i;
            if((l < heapSize) && (heapArray[l] > heapArray[i])){
                largest = l;
            }
            if((r < heapSize) && (heapArray[r] > heapArray[largest])){
                largest = r;
            }
            if(largest != i){
                int temp = heapArray[i];
                heapArray[i] = heapArray[largest];
                heapArray[largest] = temp;
                Max_heapify(largest);
            }
        }
        //function to turn an entire array into a maximum heap
        public void BuildMaxHeap(){
            for(int i = (heapSize/2)-1; i >= 0; i--){
                Max_heapify(i);
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
         * function to remove the largest number from the heap and returns it
         * and then maintains its max heap form
         */
        
        public int ExtractMax(){
            int max = heapArray[0];
            heapArray[0] = heapArray[heapSize-1];
            heapSize--;
            Max_heapify(0);
            return max;
        }
        /*
         * function that increases the value at a "node"
         * @param index is the position on the array of the node
         * @param newValue is the new value for the node
         */
        
        public void Increase(int index, int newValue) throws IOException {
            if(index < 0 || index > (heapSize-1) || newValue <= heapArray[index] ){
                throw new IOException("INDEX OUT OF BOUNDS OR NEW VALUE TOO SMALL");
            }
            else{
                heapArray[index] = newValue;
                int p = parent(index);
                while(p>=0 && heapArray[index] > heapArray[p]){
                    int temp = heapArray[index];
                    heapArray[index] = heapArray[p];
                    heapArray[p] = temp;
                    index = p;
                    p = parent(index);
                }
                
            }
        }
        /*
         * function to decrease the value at a "node"
         * @param index is the position on the array of the node
         * @param newValue is the new value for the node
         */
        public void Decrease(int index, int newValue) throws IOException {
            if(index < 0 ||  index > (heapSize-1) || heapArray[index] <= newValue){
                throw new IOException("INDEX OUT OF BOUNDS OR NEW VALUE TOO LARGE");
            }
            else{
                heapArray[index] = newValue;
                Max_heapify(index);  
            }
        }
        /*
         * function to modify the value at a "node" using the Increase
         * and Decrease member functions
         * @param index is the position on the array of the node
         * @param newValue is the new value for the node
         */
        public void Update(int index, int newValue) throws IOException {
            if(index < 0 || index > (heapSize-1)){
                throw new IOException("INDEX OUT OF BOUNDS");
            }
            else if(heapArray[index] > newValue){
                Decrease(index, newValue);
            }
            else{
                Increase(index, newValue);
            }
        }
        /*
         * function that searches the heap for a particular key and returns
         * its position if present and -1 if not present
         * @param key is the value being searched for
         * @param index is the index of the node being searched
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
        /*
        BinHeap BH = new BinHeap(11);
        BH.heapArray[0] =56;
        BH.heapArray[1] =61;
        BH.heapArray[2] =89;
        BH.heapArray[3] =101;
        BH.heapArray[4] =125;
        BH.heapArray[5] =167;
        BH.heapArray[6] =233;
        BH.heapArray[7] =401;
        BH.heapArray[8] =555;
        BH.heapArray[9] =1004;
        BH.heapArray[10] = 110;
        BH.BuildMaxHeap();
        for(int i = 0; i<BH.heapSize; i++){
            System.out.print(BH.heapArray[i] + " ");
        }
        System.out.print("\n");
        BH.addElement(250);
        try{
        BH.search(110);
        }
        catch(IOException e){
            System.out.println(e.getMessage());
        }
        for(int i = 0; i<BH.heapSize; i++){
            System.out.print(BH.heapArray[i] + " ");
        }
        */
    }
        
}

