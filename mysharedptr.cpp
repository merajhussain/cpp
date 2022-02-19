
#include <iostream>
#include <math.h>
#include<string>
using namespace std;

template<class T>
class my_shared_ptr
{
    int* ref_count;
    T* m_ptr;
   

    
public:

    my_shared_ptr(T val)
    {
        m_ptr = new T;
        *m_ptr = val;
        ref_count = nullptr;
      
        if (ref_count)
        {
            ++(*ref_count);
        }
        else
        {
            ref_count = new int;
            *ref_count = 1;
            m_ptr = new T;
            *m_ptr = val;
            cout << "memeory allocated" << endl;
        }
    }

    my_shared_ptr( my_shared_ptr<T>& src)
    {
        
        if (src.isValid())
        {
            if (this->isValid()) this->reset();
            this->m_ptr = src.m_ptr;
            this->ref_count = src.ref_count;
            (*ref_count)++;
            this->isOwner = false;
        }

         
    }

    my_shared_ptr<T>& operator=(  my_shared_ptr<T>& src)
    {
        if (src.isValid())
        {
            this->reset();
            this->m_ptr = src.m_ptr;
            this->ref_count = src.ref_count;
            (*ref_count)++;
            this->isOwner = false;
            
        }

        return *this;
    }


    T* get()
    {
        return m_ptr;
    }

    T getVal()
    {
        if (m_ptr) return *m_ptr;

        return T();
    }

    int get_reference_count()
    {
        if (isValid()) return *ref_count;
        return 0;
    }

    void increase_ref_count()
    {
        if (ref_count) ++(*ref_count);
    }
    

    void reset()
    {
       
        if (ref_count)
        {
            if (*ref_count == 1)
            {
                if (m_ptr) delete m_ptr;
                delete ref_count;
                m_ptr = ref_count = nullptr;
            }
            else
            {
                --(*ref_count);
                this->m_ptr = nullptr;
                this->ref_count = nullptr;
            }
          
        }
       
         
    }

    bool isValid()
    {
        if (ref_count && m_ptr && *ref_count>0) return true;

        
        return false;
    }

    void setVal(T val)
    {
        if (this->isValid())
        {
            *m_ptr = val;
        }
    }

    void dumpConents()
    {
         
        cout << "==========start of the dump========================" << endl;
        cout << this->get() << endl;
        cout << this->getVal() << endl;
        cout << this->get_reference_count() << endl;
       
       // cout << ((isOwner) ? "isOwner=true" : "isOwner=false") << endl;
        cout <<  (isValid()? "isValid=true" : "isValid=false") << endl;
        cout << "==================================" << endl;
    }
    ~my_shared_ptr()
    {
        
        if (ref_count)
        {
            if (*ref_count == 1)
            {
                *ref_count = 0;
                if (m_ptr)  delete m_ptr;
                ref_count = nullptr;
                m_ptr = nullptr;
                cout << "memory cleaned" << endl;
            }
            else
            {
                --(*ref_count);
            }
        }

    }


};

int main() {

    my_shared_ptr<int> sptr(2);
    
 
    auto sptr2(sptr);

   

    auto spr3 = sptr;

    spr3.setVal(10);
    sptr.dumpConents();
    sptr2.dumpConents();
    spr3.dumpConents();

   // spr3.reset();
   // sptr2.reset();
    //sptr.reset();
    sptr.dumpConents();
    sptr2.dumpConents();
    spr3.dumpConents();

    my_shared_ptr<int> msp1(100);
    spr3 = msp1;


    sptr.dumpConents();
    sptr2.dumpConents();

    msp1.dumpConents();
    spr3.dumpConents();

    sptr.dumpConents();
    spr3 = sptr;

  
    msp1.dumpConents();
    spr3.dumpConents();
    sptr.dumpConents();


   
    return 0;
}
