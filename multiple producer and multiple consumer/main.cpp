#include <bits/stdc++.h>
#include <queue>
#include <thread>
#include <windows.h>
using namespace std;

queue <int> b;					//b is the buffer
int semaphore=1;
int empt_slots=5,full_slots=0;					//empt_slots is the number of empty slots in buffer while full_slots is number of full slots in buffer
int print=1;
long item=1;

void wait(int &a){
	while(a<=0){
        Sleep(1);
	}
	a--;
}

void signal(int &a){
	a++;
}

void producer(int n){
    wait(print);
	cout<<"\nProducer "<<n<<" Entered\n";
	signal(print);
	int p=1;
	while(p<4){
		wait(empt_slots);
		wait(semaphore);
		item=item*3;
		wait(print);
		printf("Producer %d produced: %d\n",n,item);
		signal(print);
		p=p+1;
		b.push(item);
		signal(semaphore);
		signal(full_slots);
	}
	wait(print);
	cout<<"\nProducer "<<n<<" Exited\n";
	signal(print);
}

void consumer(int n){
    wait(print);
	cout<<"\nConsumer "<<n<<" Entered\n";
	signal(print);
	int c=1;
	while(c<4){
		wait(full_slots);
		wait(semaphore);
		wait(print);
		printf("Consumer %d consumed: %d\n",n,b.front());
		signal(print);
		c=c+1;
		b.pop();
		signal(semaphore);
		signal(empt_slots);
	}
	wait(print);
	cout<<"\nConsumer "<<n<<" Exited\n";
	signal(print);
}

int main(){
	cout<<"Maximum size of buffer is taken as 5\nNumber of Producers is 5\nNumber of Consumers is 5\n";
    cout<<"Maximum number of items a producer can produce & a consumer can consume is 3\n";
	thread t[10];
	for(int i=0;i<10;i=i+2){
        int n=i/2+1;
        t[i]=thread(producer,n);
        t[i+1]=thread(consumer,n);
	}
	for(int i=0;i<10;i++){
        t[i].join();
	}
	return 0;
}
