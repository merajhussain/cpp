#include<iostream>

using namespace std;

typedef unsigned long long ull;
template<class T>
struct Node 
{
   
    public:
	    
	    Node *next;
	    T data;

	    ~Node()
	    {

	    }

};


template<class T>
class LinkedList
{

	Node<T> *head;
	ull size;

	public:
	LinkedList()
	{
		size = 0;
		head = nullptr;
	
	}



        

        T get(ull index)
	{
		Node<T> *cur = head;
		for(ull i=1;i<index;i++)
		{
                     cur = cur->next;
		}

		if(cur) return cur->data;

		return T();
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
			     size++;

			}
		}
	}

	void print()
	{
		if(!head) 
		{
			cout << "list empty"<<endl;
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

	bool remove(T val)
	{

		auto temp = head;
		Node<T> *prev = nullptr;

		while(temp != nullptr)
		{

			if(temp)
			{
				if ( temp->data == val )
				{

					if( prev == nullptr)//prev is null only if the the val matches head data
					{
						head = head->next;
						
						delete temp;

						return true;
					}
					else
					{
                         		    prev->next = temp->next;
					    delete temp;

					    return true;

					}
				}
			}


			prev = temp;
			temp = temp->next;
		}

		if(temp == nullptr) return false;

		return true;
	}


	~LinkedList()
	{

		if( head)
		{



			auto temp = head;
			auto next = temp;
			while(temp != nullptr)
			{
				
				if(temp) 
				{
					next = temp->next;
					delete temp;
				}

				temp = next;
			}

			head = nullptr;
			size=0;
		}
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
        cout<<ls.getSize()<<endl;
	ls.remove("w5");
	ls.print();
	ls.remove("w2");
	ls.print();
	 


     
	return 0;
}
