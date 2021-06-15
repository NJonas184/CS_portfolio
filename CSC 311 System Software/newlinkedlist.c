#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>


int choice = 10; //While loop condition
int choiceKey; //User input for key
int choiceValue; //User input for value
int searchKey; //User search key
typedef struct listNode{ //Struct for Nodes
	int key;
	int value;
	struct listNode* next;	
}Node;

	
typedef struct SLL { //Struct for Linked List
	struct listNode* head;
	struct listNode* tail;
}LinkedList;


void addLast(LinkedList* list, int funcKey,int funcValue){//Adds node to tail of SLL
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->key=funcKey;
	newNode->value=funcValue;
	newNode->next = NULL;

	if(list->head==NULL){
		list->head=newNode;
		list->tail=newNode;
	}
	else {
		list->tail->next=newNode;
		list->tail=newNode;	
	}//if
	printf("Added node successfully.\n");
}//addLast
void addFirst(LinkedList* list, int funcKey,int funcValue){//Adds node to heal of SLL
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->key=funcKey;
	newNode->value=funcValue;
	if(list->head==NULL){
		list->head=newNode;
		list->tail=newNode;
		newNode->next=NULL;
	}
	else {
		newNode->next=list->head;
		list->head=newNode;	
	}//if
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

Node* search(LinkedList* list, int searchKey){//Searches for the key of a node in a SLL
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

void addAfter(LinkedList* list, int searchKey, int funcKey, int funcValue){//Inserts a node after a specified node using a key
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->key=funcKey;
	newNode->value=funcValue;
	Node* searchNode = search(list,searchKey);
	if(searchNode != NULL){
		if(searchNode == list->tail){
			newNode->next = searchNode->next;
			searchNode->next = newNode;
			newNode->next = NULL;			
		}
		else{
			newNode->next = searchNode->next;
			searchNode->next = newNode;
		}//Inner if
	}//Outer if
}//addAfter

void update(LinkedList* list, int searchKey, int updateValue){//Updates the value of a node
	Node* temp = search(list,searchKey);
	if(temp != NULL){
		temp->value = updateValue;
		printf("Node updated:\n");
		printNode(temp);
	}
	else{
		printf("Node does not exist.\n");
	}
}//update

int removeNode(LinkedList* list, int searchKey){//Removes a node from the SLL	
	Node* temp = list->head;
	Node* rewind = temp;
	if(temp == NULL){
		printf("Please add nodes before trying to remove them.\n");
		return 1;	
	}//if to check if temp empty
	while(temp->key != searchKey){
		rewind = temp;
		temp=temp->next;					
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

int main(){

	LinkedList* linkedlist = (LinkedList*) malloc(sizeof(LinkedList));
	linkedlist->head=NULL;
	linkedlist->tail=NULL;

	while(choice!=7){
		printf("Linked List Generator, please select what you would like to do:\n");
		printf("[1] Add front node\n");
		printf("[2] Add last node\n");
		printf("[3] Add new node after specified node\n");
		printf("[4] Search specified node\n");
		printf("[5] Print all nodes\n");
		printf("[6] Update a specified node\n");
		printf("[7] Quit\n");
		printf("[8] Remove a node\n");
		printf("Please type in a number from 1-8 to indicate your choice:\n");
		scanf("%d",&choice);

		switch(choice){
		case 1:
			printf("Please select a key for the new element:\n");
			scanf("%d",&choiceKey);
			printf("Please select a value for the new element:\n");
			scanf("%d",&choiceValue);
			addFirst(linkedlist,choiceKey,choiceValue);
			break;
		case 2:
			printf("Please select a key for the new element:\n");
			scanf("%d",&choiceKey);
			printf("Please select a value for the new element:\n");
			scanf("%d",&choiceValue);
			addLast(linkedlist,choiceKey,choiceValue);
			break;
		case 3:
			printf("Please enter the key of the element that you want the new element after:\n");
			scanf("%d",&searchKey);
			printf("Please select a key for the new element:\n");
			scanf("%d",&choiceKey);
			printf("Please select a value for the new element:\n");
			scanf("%d",&choiceValue);
			addAfter(linkedlist,searchKey,choiceKey,choiceValue);
			break;
		case 4:	
			printf("Please enter the key you want to search:\n");
			scanf("%d",&searchKey);
			search(linkedlist, searchKey);
			break;
		case 5:
			print(linkedlist);
			break;
		case 6:
			printf("Please enter the key of the value you wish to change:\n");
			scanf("%d",&searchKey);
			printf("Please enter the new value:\n");
			scanf("%d",&choiceValue);
			update(linkedlist,searchKey, choiceValue);
			break;
		case 7:
			printf("Have a nice day!\n");
			break;
		case 8:
			printf("Please enter the key of the node you wish to delete:\n");
			scanf("%d",&searchKey);
			removeNode(linkedlist,searchKey);
			break;
		default:
			printf("Please enter a valid number between 1-8\n");
			break;
		}//End of switch
	}//End of While loop	
}//main

