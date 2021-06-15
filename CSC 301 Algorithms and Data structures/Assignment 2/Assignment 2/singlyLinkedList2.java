public class SinglyLinkedList {
   public Object item;
   public Node next;
 }

 public class SinglyLinkedList<T> {
   private ListNode<T> head;
   private ListNode<T> tail;
   private int nodeCount;

 public LinkedList() {
   this.size = 0;
   this.head = null;
 }
 
 */
	public void insertNode(String item) {
		Node node = new Node();
		node.item = item;
		Node current = this.head;

		if (this.head == null) {
			this.head = node;
			this.head.next = null;
			this.size = 1;
			System.out.println(this.head.toString());
		} else {

			while (current.next != null) {
				current = current.next;
			}
			current.next = node;
			node.next = null;
			this.size += 1;
		}
	}

	/**
	 * Adding node at the first location of the linked list
	 *
	 * @param item - represent item of the node to be added to LL
	 */


	/**
	 * Adding node at the nth location of the linked list
	 *
	 * @param item - represent the item of the node to be added to the list
	 * @param position - position at which the node is to be added
	 */
   public void addLast(String item, int position) {
		Node node = new Node();
		node.item = item;
		Node current = this.head;
		if (this.head != null && position <= this.size) {
			for (int i = 1; i < position; i++) {
				current = current.next;
			}
			node.next = current.next;
			current.next = node;
			this.size += 1;
		}else{
			System.out.println("Exceeded the linked list size. Current Size: "+size);
		}
	}
/**
  * @param location - Find item at location
  *
  */
 public void findNodeAt(int location) {
   Node node = this.head;
   if(head !=null && location<= size){
     for(int i=0;i<location;i++){
       node = node.next;
     }
     System.out.println("Node item at location "+location+" is "+node.item);
   }
 }

 /**
  * Find the item at the last location
  *
  */
 public void findLastNode() {
   Node node = this.head;
   if(head != null){
     for(int i=0;i<size-1;i++){
       node = node.next;
     }
     System.out.println("Node item at last location is "+node.item);
   }
 }
 /**
	 * Printing all the items in the list
	 */
	public void printNodes() {
		if (this.size < 1)
			System.out.println("There are no nodes in the linked list");
		else {
			Node current = this.head;
			for (int i = 0; i < this.size; i++) {
				System.out.println("Node " + current.item + " is at location " + i);
				current = current.next;
			}
		}
	}
  /**
	 * Obtain the current size of the list
	 * @return
	 */
	public int getListSize(){
		return size;
	}

}
public class Main {

 public static void main(String[] args) {
   LinkedList list = new LinkedList();

   System.out.println("Current Size of the list is: "+list.getListSize());

   list.insertNode("test1");
   list.insertNode("test2");
   list.insertNode("test3");
   list.insertNode("test4");
   list.insertNode("test5");
   list.insertNode("test6");
   list.insertNode("test7");
   list.printNodes();

   System.out.println();

   System.out.println("Finding item test2 in the Linked list");
   list.findNode("test2");
   System.out.println("Finding item nonExist in the Lineked list");
   list.findNode("nonExist");

   System.out.println();

   System.out.println("Finding item at location 4");
   list.findNodeAt(4);

   System.out.println();
   System.out.println("Finding item at last location ");
   list.findLastNode();

   System.out.println();

   System.out.println("Current Size of the list is: "+list.getListSize());
   System.out.println("Adding test1st at start of the Node");
   list.insertFirst("test1st");
   list.printNodes();

   System.out.println();

   System.out.println("Current Size of the list is: "+list.getListSize());
   System.out.println("Adding testNth at 2nd Location");
   list.insertNth("testNth", 2);
   list.printNodes();

   System.out.println();

   System.out.println("Current Size of the list is: "+list.getListSize());
   System.out.println("Deleting node from 4th location");
   list.deleteNthNode(4);
   list.printNodes();
 }

}
