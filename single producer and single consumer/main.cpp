#include <bits/stdc++.h>
#include <queue>
#include <thread>
#include <windows.h>
using namespace std;

queue <int> b;					//b is the buffer
int semaphore=1,item=1;
int empt_slots=5,full_slots=0;					//empt_slots is the number of empty slots in buffer while full_slots is number of full slots in buffer
int print=1;

void wait(int &a){
	while(a<=0){
        Sleep(0.5);
	}
	a--;
}

void signal(int &a){
	a++;
}

void producer(){
    wait(print);
	cout<<"\nProducer Entered\n";
	signal(print);
	while(empt_slots!=0){
		wait(empt_slots);
		wait(semaphore);
		item=item*5;
		wait(print);
		printf("Producer produced: %d\n",item);
		signal(print);
		b.push(item);
		signal(semaphore);
		signal(full_slots);
	}
	wait(print);
	cout<<"\nProducer Exited\n";
	signal(print);
}

void consumer(){
    wait(print);
	cout<<"\nConsumer Entered\n";
	signal(print);
	while(full_slots!=5);
	while(full_slots!=0){
		wait(full_slots);
		wait(semaphore);
		wait(print);
		printf("Consumer consumed: %d\n",b.front());
		signal(print);
		b.pop();
		signal(semaphore);
		signal(empt_slots);
	}
	wait(print);
	cout<<"\nConsumer Exited\n";
	signal(print);
}

int main(){
	cout<<"Maximum size of buffer is taken as 5";
	thread produce(producer);

	thread consume(consumer);
	produce.join();
	consume.join();
	return 0;
}
