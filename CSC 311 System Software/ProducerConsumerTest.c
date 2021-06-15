#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include<pthread.h>
#include<unistd.h> //unix standard


typedef struct threadVariable{ //Structure to passe through thread functions
	int buffSize;
	int * arrP;
	int front;
	int rear;
	pthread_mutex_t producerLock;
	pthread_mutex_t consumerLock;
	pthread_cond_t producerSignal;
	pthread_cond_t consumerSignal;
	int producerSleep;
	int consumerSleep;
	bool terminated; //Variable to help terminate the threads
} threadVars;


bool isFull(int front, int end, int size){//Checks to see if the array is full
	if((front == end + 1) || (front == 0 && end == size-1)){//Two checks for if the queue is full
		return true;
	}//if
	return false;
}//isFull

bool isEmpty(int front){//Checks to see if the array is empty by checking the front index
	if(front == -1){
		return true;
	}
	return false;
}//isEmpty


void *consumeFunction(void *consv){//Consumes elements within an array
	threadVars* conVar = (threadVars*)consv;
	while(conVar->terminated);
	while(!conVar->terminated){
		pthread_mutex_lock(&(conVar->consumerLock));
		if(isEmpty(conVar->front)){
			printf("Queue is empty, producer needs to produce.\n");
		}//if
		else{
			int num = conVar->arrP[conVar->front];
			if(conVar->front == conVar->rear){//Last number
				conVar->front = -1;
				conVar->rear = -1;
			}//if
			else{
				conVar->front = (conVar->front + 1) % conVar->buffSize;
			}//else
			printf("Removed %d\n",num);
		}//else
		pthread_cond_signal(&(conVar->producerSignal));
		pthread_mutex_unlock(&(conVar->consumerLock));
		sleep(conVar->consumerSleep);
	}//while
	pthread_exit(NULL);
}//consume

void *produceFunction(void *prodv){//Produces elements for an array
	threadVars* proVar = (threadVars*)prodv;
	while(proVar->terminated);//Wait for all threads to be created
	while(!proVar->terminated){//All threads are created
		pthread_mutex_lock(&(proVar->producerLock));//lock the lock
		if(isFull(proVar->front,proVar->rear,proVar->buffSize)){
			printf("Queue is full, consumer needs to consume.\n");
		}//if
		else{
			if(proVar->front == -1){ //empty
				proVar->front = 0;
			}//if
			int randomNum= rand() % 100 + 1;//random number between 1 and 100
			proVar->rear = (proVar->rear + 1) % proVar->buffSize;//Add it to the circ queue
			proVar->arrP[proVar->rear] = randomNum;
			printf("Inserted %d\n", randomNum);
		}//else
		pthread_cond_signal(&(proVar->consumerSignal));//Send signal to the consumer threads to work
		pthread_mutex_unlock(&(proVar->producerLock));//unlock the lock
		sleep(proVar->producerSleep);//sleeptime
	}//while
	pthread_exit(NULL);
}//produce


int main(){
	srand(time(NULL));
	// FILE FORMATE == buffSize,proSleep,conSleep,numP,numC,time
	FILE * filePointer;//Creates file pointer
	char * line = NULL; //Creates line tracker
	size_t len = 0;//Length
	ssize_t read;//getLine variable

	filePointer = fopen("testConfig.txt", "r");//open file
	if(filePointer==NULL){//if file is missing
		printf("File missing\n");
		return 0;
	}
	
	while((read = getline(&line, &len, filePointer)) != -1){//getLine loop
		int bufferSize;
		int proSleep;//producerSleep
		int conSleep;//consumerSleep
		int numP;
		int numC;
		int testTime;//Testcase timespan
		char * split;// split pointer
		split = strtok(line, ",");//split by commas
		for(int i = 0; i<6; i++){//Always 5 variables
			if(split != NULL){
				switch(i){//Switch statement to grab all variables and print them
				case 0:
					bufferSize = atoi(split);
					printf("buffSize = %d, ", bufferSize);
					break;
				case 1:
					proSleep = atoi(split);
					printf("proSleep = %d, ", proSleep);
					break;
				case 2:
					conSleep = atoi(split);
					printf("conSleep = %d, ", conSleep);
					break;
				case 3:
					numP = atoi(split);
					printf("numP = %d, ", numP);
					break;
				case 4:
					numC = atoi(split);
					printf("numC = %d, ", numC);
					break;
				case 5:
					testTime = atoi(split);
					printf("time = %d.", testTime);
					break;
				}//switch
				split = strtok(NULL, ",");// Stop
			}//if
		}//for loop
		printf("\n");

		pthread_t consumer[numC];//Creating threads
		pthread_t producer[numP];
		int array[bufferSize];

		threadVars testCase;
		testCase.buffSize = bufferSize;
		testCase.producerSleep = proSleep;
		testCase.consumerSleep = conSleep;
		testCase.front = -1;//starting indexes
		testCase.rear = -1;
		testCase.arrP = array;
		testCase.terminated = true;//variable for while loop

		pthread_mutex_init(&testCase.producerLock,NULL);//Creating locks and conditions
		pthread_mutex_init(&testCase.consumerLock,NULL);
		pthread_cond_init(&testCase.producerSignal,NULL);
		pthread_cond_init(&testCase.consumerSignal,NULL);
	
		for(int i = 0;i<numP+numC;i++){
			if(i<numP){
				pthread_create(&producer[i],NULL, produceFunction, (void *)&testCase);
			}
			else{
				pthread_create(&consumer[i-numP],NULL, consumeFunction, (void *)&testCase);
			}
		}//for loop for creating producers and consumers
	
		testCase.terminated = false;
		sleep(testTime);//Tells threads to stop after a certain amount of time
		testCase.terminated = true;
			
		for(int i = 0;i<numP+numC;i++){
			if(i<numP){
				pthread_join(producer[i],NULL);//Terminate remaining threads
			}
			else{
				pthread_join(consumer[i-numP],NULL);//same as above
			}
		}//for loop for creating producers and consumers
	}//while loop
	fclose(filePointer);
	free(line);
	return 0;
}//main
