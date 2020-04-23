#include<iostream>
using namespace std;
struct Queue {
    int front, rear, capacity;
    int* queue;
    Queue(int c)
    {
        front = rear = 0;
        capacity = c;
        queue = new int;
    }

    ~Queue() { delete[] queue; }

    // function to insert an element
    // at the rear of the queue
    void queueEnqueue(int data)
    {
        // check queue is full or not
        if (capacity == rear) {
            cout<<"\nBuffer is full\n";
            return;
        }

        // insert element at the rear
        else {
            queue[rear] = data;
            rear++;
        }
        return ;
    }

    // function to delete an element
    // from the front of the queue
    void queueDequeue()
    {
   if (front == - 1 || front > rear) {
      cout<<"Queue Underflow ";
   return ;
   } else {
      cout<<"Element consumed from buffer is : "<< queue[front] <<endl;
      front++;;
   }
    }
    // print queue elements
    void queueDisplay()
    {
        int i;
        if (front == rear) {
            printf("\nBuffer is Empty\n");
            return;
        }

        // traverse front to rear and print elements
        for (i = front; i < rear; i++) {
            cout<<queue[i]<<" ";
        }
        return;
    }
};

void wait(int &x)
{
    if(x>0)
    x--;
}
void signal(int &x)
{
    x++;
}
int main()
{

    int i,n;
    cout<<"Producer Consumer Problem Simple Implementation"<<endl;
    cout<<"Enter the size of buffer:";
    cin>>n;

    Queue q(n);
    int empty=n;
    int full=0;
    int mutex=1;
    while(1){

            cout<<endl<<"Enter your choice 1.Produce 2.Consume"<<endl;
            int x;
            cin>>x;
            if(x==1)
            {
                if(empty!=0 && mutex==1)
                {
                    cout<<"Enter the value:"<<endl;
                    wait(empty);
                    wait(mutex);
                    int val;
                    cin>>val;
                    q.queueEnqueue(val);
                    signal(mutex);
                    signal(full);
                }
            else {
                    cout<<"Buffer is full"<<endl;
                    q.queueDisplay();

            }
            }
            else if(x==2){
                if(full>0 && mutex==1)
                {
                    wait(full);
                    wait(mutex);
                    q.queueDequeue();
                    signal(mutex);
                    signal(empty);
                }
                else {
                        cout<<"Buffer is empty"<<endl;
                        break;
                }

            }else break;

            }

             return 0;


    }

