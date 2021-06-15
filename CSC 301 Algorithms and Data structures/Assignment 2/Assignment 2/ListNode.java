/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nicholasjonas
 */
public class ListNode<T> {
    private T data;
    private ListNode<T> next;
    
    public ListNode(T data){
        this.data = data;
        next = null;
    }
    
    public T getData(){
      return data;  
    }
    
    public ListNode<T> getNext(){
        return next;
    }
    
    public void setData(){
        this.data = data;
    }
    
    public void setNext(ListNode<T> next){
        this.next = next;
        
    }
    
}
