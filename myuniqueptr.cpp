#include<iostream>
#include<string>
using namespace std;

template<class T>
class my_unique_ptr
{

	T* m_ptr;
public:
	my_unique_ptr(T val)
	{
		m_ptr = new T;
		*m_ptr = val;
	}

	my_unique_ptr( my_unique_ptr& src)
	{
		this->m_ptr = src.m_ptr;
		src.m_ptr = nullptr;

	}
	my_unique_ptr& operator=(  my_unique_ptr& src)
	{
		this->m_ptr =  src.m_ptr;
		src.m_ptr = nullptr;
	}
	void reset()
	{
		delete m_ptr;
		m_ptr = nullptr;

	}

	T operator*()
	{
		if (m_ptr) return *m_ptr;
		return T();
	}

	T* get()
	{
		return m_ptr;
	}

	T* release()
	{
		T* temp = new T;
		*temp = *m_ptr;
		delete m_ptr;
		m_ptr = nullptr;
		return temp;

	}

	~my_unique_ptr()
	{
		if (m_ptr)
		{
			delete m_ptr;
			m_ptr = nullptr;
		}
		
	}

};
int main()
{

	my_unique_ptr<int> muptr(2);

	auto p2(muptr);
	cout << *p2 << endl;

	 
	unique_ptr<int> mu(new int);
	*mu = 11;
	cout << *mu << endl;
	


	return 0;
}
