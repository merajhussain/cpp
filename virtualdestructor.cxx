#include<iostream>
using namespace std;

class base
{
    public:
    void fun()
    {
           cout <<"base"<<endl;
    }

    virtual  ~ base()
    {
        cout << "base destoryed"<<endl;
    }
};

class dervied : public base
{
      public:
      void fun()
      {
          cout<<"dervied"<<endl;
      }

   ~ dervied()
   {
       cout << "child destroyed"<<endl;
   }
   
};
int main()
{
   base *b = new dervied();

   delete b;

   b = nullptr;//doesn't really matter here
    return 0;
}