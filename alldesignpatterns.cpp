
#include <iostream>
#include <thread>
#include <vector>
#include <list>
#include<mutex>
using namespace std;
mutex gmtx;

//singleton
class singleton
{

    singleton()
    {
        cout << "singleton instance created" << endl;
    }

public:
    static singleton* getInstance()
    {
        lock_guard<mutex> lock(gmtx);
        if (instance == nullptr)
        {
            instance = new singleton();
        }

        return instance;
       
    }

    static singleton& mayers_singleton()
    {
        static singleton s;
        return s;
    }

      inline static singleton* instance;
};
//================================================================end singleton================================//
//factory
class iproduct
{


public:
    virtual void details() = 0;
};

class product1 :public iproduct
{
public:

    product1()
    {
        cout << "product1 created" << endl;
    }

    void details()
    {
        cout << "product1 details" << endl;
    }

};

class product2 : public iproduct
{
public:
    product2()
    {
        cout << "product2 created" << endl;
    }
    void details()
    {
        cout << "product2 details " << endl;
    }

};
using producttype = enum{p1,p2};

iproduct* factory_create(int type)
{
    switch (type)
    {
    case p1:
        return new product1();
        break;
    case p2:
        return new product2();
        break;

        default:
            cout << "factory creation failed, unsupported product type" << endl;
            break;

    }

}
//==========================end factory==============================

//observer

class iobserver
{

public:
    virtual void update() = 0;

   

};



using ObserverSPtr = shared_ptr<iobserver>;
class isubject
{
public:  

    virtual void notifyall() = 0;
    virtual void attach(ObserverSPtr obserber) = 0;
    virtual void detach(ObserverSPtr obserber) = 0;
    virtual int totalObservsers() = 0;

    virtual int&  getState() = 0;
    virtual void setState(int state) = 0;

     
};


using ObserverList = list< ObserverSPtr>;
using SubjectSptr = shared_ptr<isubject>;



class Subject :public isubject
{
    int state;
    ObserverList subscribed_observers;

public:

    
    Subject()
    {
        state = -1;
        subscribed_observers.clear();
        cout << "subject created" << endl;
    }
    void attach(ObserverSPtr observer)
    {
        subscribed_observers.push_back(observer);
    }

    void detach(ObserverSPtr observer)
    {
        subscribed_observers.remove(observer);
    }

    void notifyall()
    {
        for (auto &observer : subscribed_observers)
        {
            observer->update();
        }
    }

    int& getState()
    {
        return state;
    }

    void setState(int state)
    {
       this->state = state;
       this->notifyall();
    }

    int totalObservsers()
    {
        return subscribed_observers.size();
    }

    ~Subject()
    {
        cout << "destroyed subject" << endl;
    }

};

class Observer :public iobserver
{
    weak_ptr<isubject> subject;
public:
   


    Observer( SubjectSptr subject)
    {
        this->subject = subject;
        cout << "observer created" << endl;
        
    }
    void update()
    {
        cout << "Subject got updated to new state:" << subject.lock()->getState() << endl;
        
    }

     ~Observer()
    {
        cout << "destroyed observer" << endl;
    }
};




int main()
{
    //singleton
    thread t1(singleton::mayers_singleton);
    thread t2(singleton::mayers_singleton);
    thread t3(singleton::mayers_singleton);

    thread t4(singleton::getInstance);
    thread t5(singleton::getInstance);
    thread t6(singleton::getInstance);


    t1.join();
    t2.join();
    t3.join();

    t4.join();
    t5.join();
    t6.join();

    //factory
    auto pr1 = factory_create(p1);
    auto pr2 = factory_create(p2);
    auto pr3 = factory_create(-1);
    pr1->details();
    pr2->details();

    //observer
    /*
     1.subject
     2.observer
     
    
    */

    auto subject = make_shared<Subject>();
    auto observer1 = make_shared<Observer>(subject);
    auto observer2 = make_shared<Observer>(subject);
    auto observer3 = make_shared<Observer>(subject);
    subject->attach(observer1);
    subject->attach(observer2);
    subject->attach(observer3);
    subject->setState(2);
    subject->detach(observer3);
    
    subject->setState(3);

    
  
    return 0;

}


