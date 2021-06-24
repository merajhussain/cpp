#include<iostream>

using namespace std;

typedef unsigned long long ull;
template<class T>
class Node 
{
   
    public:
	    
	    Node *next;
	    T data;

};


template<class T>
class LinkedList
{

	Node<T> *head;
	ull size;

	public:
	LinkedList()
	{
		size =0;
		head = nullptr;
	
	}
        




	void add(T data)
	{

		if(!head)
		{
			head = new Node<T>();
			head->next = nullptr;
			head->data = data;
			size++;
		}
		else
		{
			Node<T> *cur = head;
			while(cur->next !=nullptr)
			{ 
			     cur = cur->next; 

			} 

			if(cur)
			{
			     Node<T> *temp= new Node<T>();	
                             temp->data = data;
                             temp->next = nullptr;
                             cur->next = temp;

			}
		}
	}

	void print()
	{
		if(!head) 
		{
			cout << "list empty";
			return;
		}

		Node<T>* cur = head;

		while(cur->next != nullptr)
		{
			cout<<cur->data<<"->";
			cur = cur->next;
		}
		cout<<cur->data<<endl;
	}

	void reverse()
	{
		if(head)
		{


			Node<T> * prev = nullptr;
			Node<T> * cur = head;
			Node<T> * next = nullptr;

			while(cur->next != nullptr)
			{
				next = cur->next;
				cur->next = prev;
				prev = cur;
				cur = next;
			
			}
                                        
			cur->next = prev;

			head = cur;
		}
	}

	ull getSize()
	{
		return size;
	}


	~LinkedList()
	{

		Node<T> *temp = head;
		while(temp != nullptr)
		{
			if(temp) delete temp;

			temp = temp->next;
		}

		head = nullptr;
		size=0;
	}
};


int main()
{



	LinkedList<int> ll;

	for(int i=1;i<10;i++)
	{
		ll.add(i);
	}
	ll.print();
	ll.reverse();
	ll.print();

	LinkedList<string> ls;
	ls.add("w1");
	ls.add("w2");
	ls.add("w3");
	ls.add("w4");
	ls.add("w5");
	ls.print();
	ls.reverse();
	ls.print();

	return 0;
}
