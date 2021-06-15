#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef struct listNode{ //Struct for Nodes
	int key;
	int value;
	struct listNode* next;	
}Node;

	
typedef struct SLL { //Struct for Linked List
	struct listNode* head;
	struct listNode* tail;
}LinkedList;

Node* createNode(int nodeKey, int nodeValue){
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->key=nodeKey;
	newNode->value=nodeValue;
	newNode->next = NULL;
	return newNode;

}//createNode

void addLast(LinkedList* list){//Adds node to tail of SLL
	int choiceKey; //User input for key
	int choiceValue; //User input for value
	printf("Please select a key for the new element:\n");
	scanf("%d",&choiceKey);
	printf("Please select a value for the new element:\n");
	scanf("%d",&choiceValue);
	Node* newNode = createNode(choiceKey, choiceValue);

	if(list->head==NULL){
		list->head=newNode;
	}
	else {
		list->tail->next=newNode;	
	}//if
	list->tail=newNode;//Sets tail to newNode
	printf("Added node successfully.\n");
}//addLast

void addFirst(LinkedList* list){//Adds node to heal of SLL
	int choiceKey; //User input for key
	int choiceValue; //User input for value
	printf("Please select a key for the new element:\n");
	scanf("%d",&choiceKey);
	printf("Please select a value for the new element:\n");
	scanf("%d",&choiceValue);
	Node* newNode = createNode(choiceKey,choiceValue);
	if(list->head==NULL){
		list->tail=newNode;
	}
	else {
		newNode->next=list->head;	
	}//if
	list->head=newNode;//Sets head to newNode
	printf("Added node successfully.\n");
}//addFirst

void print(LinkedList* list){//Prints the nodes of SLL
	Node* temp = list->head;	
	if(temp==NULL){
	printf("Please add nodes before printing.\n");
	}
	else{
		printf("Here are all the nodes:\n");
		while(temp!=NULL){
			printf("key: %d\n",temp->key);
			printf("value: %d\n",temp->value);
			temp=temp->next;
		}//While
	}//if else
}//print

void printNode(Node* n){//Prints a single node
	printf("Key: %d\n",n->key);
	printf("Value: %d\n",n->value);
}//printNode

Node* search(LinkedList* list, int searchKey){//General search function for all other functions that require it
	Node* temp = list->head;	
	while(temp!=NULL){
		if(temp->key == searchKey){			
			printf("Node found...\n");			
			printNode(temp);			
			return temp;		
		}//if
		temp=temp->next;
	}//while
	printf("Node doesn't exist.\n");
	return NULL;
}//search

void searchFunction(LinkedList* list){//Function that will call search function for search option
	int searchKey; //User search key
	printf("Please enter the key you want to search:\n");
	scanf("%d",&searchKey);
	search(list, searchKey);
}//searchFunction

void addAfter(LinkedList* list){//Inserts a node after a specified node using a key
	int choiceKey; //User input for key
	int choiceValue; //User input for value
	int searchKey; //User search key
	printf("Please enter the key of the element that you want the new element after:\n");
	scanf("%d",&searchKey);
	printf("Please select a key for the new element:\n");
	scanf("%d",&choiceKey);
	printf("Please select a value for the new element:\n");
	scanf("%d",&choiceValue);
	Node* searchNode = search(list,searchKey);
	if(searchNode != NULL){ //Checks to see if searchNode exists
		Node* newNode = createNode(choiceKey,choiceValue);
		if(searchNode == list->tail){
			newNode->next = searchNode->next;
			searchNode->next = newNode;		
		}
		else{
			newNode->next = searchNode->next;
			searchNode->next = newNode;
		}//Inner if
	}//Outer if
}//addAfter

void update(LinkedList* list){//Updates the value of a node
	int choiceValue; //User input for value
	int searchKey; //User search key
	printf("Please enter the key of the value you wish to change:\n");
	scanf("%d",&searchKey);
	printf("Please enter the new value:\n");
	scanf("%d",&choiceValue);	
	Node* temp = search(list,searchKey);
	if(temp != NULL){
		temp->value = choiceValue;
		printf("Node updated:\n");
		printNode(temp);
	}//if
}//update

int removeNode(LinkedList* list){//Removes a node from the SLL
	int searchKey; //User search key
	if(list->head == NULL){
		printf("Please add nodes before trying to delete any.\n");		
		return 1;
	}
	printf("Please enter the key of the node you wish to delete:\n");
	scanf("%d",&searchKey);	
	Node* temp = list->head;
	Node* rewind = list->head;
	while(temp != NULL && temp->key != searchKey){ //While to check for temp validity and key matchings
		if(temp->key != searchKey){
			rewind = temp;
			temp=temp->next;	
		}//if to check if keys match	
	}//while
	if(temp != NULL){
		if(temp == list->head && temp == list->tail){
			list->head = NULL;
			list->tail = NULL;
		}
		else if(temp == list->tail){
			list->tail = rewind;
			rewind->next = NULL;
		}
		else if(temp == list->head){
			list->head = temp->next;
		}
		else{
			rewind->next = temp->next;
		}
	}
	else{
		printf("Node does not exist.\n");	
	}
		return 0;
}//removeNode

void userInterface(){
	int choice = 10; //While loop condition
	LinkedList* linkedlist = (LinkedList*) malloc(sizeof(LinkedList));
	linkedlist->head=NULL;
	linkedlist->tail=NULL;
	Node* temp;

	while(choice!=7){
		printf("Linked List Generator, please select what you would like to do:\n[1] Add front node\n[2] Add last node\n[3] Add new node after specified node\n[4] Search specified node\n[5] Print all nodes\n[6] Update a specified node\n[7] Quit\n[8] Remove a node\nPlease type in a number from 1-8 to indicate your choice:\n");
		scanf("%d",&choice);

		switch(choice){
		case 1:
			addFirst(linkedlist);
			break;
		case 2:
			addLast(linkedlist);
			break;
		case 3:
			addAfter(linkedlist);
			break;
		case 4:	
			searchFunction(linkedlist);
			break;
		case 5:
			print(linkedlist);
			break;
		case 6:
			update(linkedlist);
			break;
		case 7:
			temp = linkedlist->head;
			while(temp != NULL){//while loop to free memory
				Node* next = temp->next;
				free(temp);
				temp = next;
			}//while loop
			
			printf("Have a nice day!\n");
			break;
		case 8:
			removeNode(linkedlist);
			break;
		default:
			printf("Please enter a valid number between 1-8\n");
			break;
		}//End of switch
	}//End of While loop	
}//userInterface

int main(){
	userInterface();
	return 0;
}//main

