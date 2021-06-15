/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nicholasjonas
 */

public class SinglyLinkedList<T> {
    private ListNode<T> head;
    private ListNode<T> tail;
    private int nodeCount;
    
    public SinglyLinkedList() {
        head = null;
        tail = null;
        nodeCount = 0;
    }
    public int size(){
        return nodeCount;
    }
    public boolean isEmpty(){
        return nodeCount == 0;
    }
    //function to add an item to the front of the linked list
    public void addFirst(T item){
        ListNode node = new ListNode(item);
        if(isEmpty()){
            tail = node;
        }
        else{
            node.setNext(head);
        }
	head = node;
	nodeCount++;
}
    //function to add an item to the back of the linked list
    public void addLast(T item){
        ListNode node = new ListNode(item);
        if(isEmpty()){
            head = node;
        }
        else{
            tail.setNext(node);
        }
        tail = node;
        nodeCount++;
    }   
    //param item - represent the node item to be added to the linked list
    public void insertNode(T item) {
        ListNode node = new ListNode(item);

        if (isEmpty()) {
            addFirst(item);
        } 
        else {
            ListNode current = head;
            while (current.getNext() != tail) {
                current = current.getNext();
            }
            current.setNext(node);
            node.setNext(tail);
            nodeCount += 1;
        }
    }
    //function to remove the first element of linked list
    public void removeFirst(){
        if(isEmpty()){
            System.out.println("ERROR: SINGLY LINKED LIST IS EMPTY");
        }
        else if(nodeCount == 0){
            tail = null;
        }
            head = head.getNext();
            nodeCount--;
            
        }
        //function to remove last elelment of linked list
    public void removeLast(){
        if(isEmpty()){
            System.out.println("ERROR: SINGLY LINKED LIST IS EMPTY");
        }
        else if(nodeCount == 0){
            head = null;
        }
            ListNode temp = head;
            while(temp != null){
                if(temp.getNext() == tail){
                    tail = temp;
                    temp.setNext(null);
                    nodeCount--;
                }
                temp = temp.getNext();
            }
    }
    //function to search for a node in a linked list with a certain key
    public ListNode search(T key){
        for(ListNode temp = head; temp != null; temp = temp.getNext()){
            if(temp.getData() == key){
                return temp;
            }
        }
        return null;
    }
    //function to remove a node from a linked list with a defined key
    public void remove(SinglyLinkedList SLL, T key){
        ListNode node = SLL.search(key);
        if(node == null)
            System.out.println("ERROR: NODE DOES NOT EXIST");
        else if(node == SLL.head)
            SLL.removeFirst();
        else if(node == SLL.tail)
            SLL.removeLast();
        else{
            ListNode temp = SLL.head;
            while(temp!= node){
                temp = temp.getNext();
            }
            temp.setNext(node.getNext());
            SLL.nodeCount--;
        }
    }
    //function to check if a node with data key is present in a linked list
    public boolean contains(SinglyLinkedList SLL, T key) {
        if(isEmpty()){
            System.out.println("ERROR: SINGLY LINKED LIST IS EMPTY");
            return false;
        }
        if(SLL.search(key) != null){
            return true;
        }
        return false;

    }
    public static void main(String args[]){
        /*
        SinglyLinkedList SLL = new SinglyLinkedList();
        SLL.addLast(27);
        SLL.addFirst("Hello");
        SLL.insertNode(2.73);
        ListNode temp = SLL.head;
        for(int i = 0; i<SLL.nodeCount;i++){
            System.out.println(temp.getData());
            temp = temp.getNext();
        }
        SLL.removeLast();
        System.out.println("Remove");
        temp = SLL.head;
        for(int i = 0; i<SLL.nodeCount;i++){
            System.out.println(temp.getData());
            temp = temp.getNext();
        }
        System.out.println(SLL.contains(SLL, 42));
        System.out.println(SLL.contains(SLL, "Hello"));
        */
    }
}
