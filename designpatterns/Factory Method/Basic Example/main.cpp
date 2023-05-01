#include "Creator.h"
#include "ConcreteCreator.h"
#include "ConcreteCreator2.h"
#include <mutex>
#include <condition_variable>
#include <iostream>
std::mutex mtx;
std::condition_variable cv;
int count = 1;
void printEven()
{
	while (count < 100)
	{
		std::unique_lock<std::mutex> lock(mtx);
		cv.wait(lock, []() {return (count % 2 == 0); });
		std::cout << count << std::endl;;
		count++;
		lock.unlock();
		cv.notify_all();

	}
	
}
void printOdd()
{

	while (count < 100)
	{
		std::unique_lock<std::mutex> lock(mtx);
		cv.wait(lock, []() {return (count % 2 != 0); });
		std::cout << count << std::endl;;
		count++;
		lock.unlock();
		cv.notify_all();

	}

}


int main() {
	ConcreteCreator2 ct ;
	ct.AnOperation() ;
	std::thread t1(printEven);
	std::thread t2(printOdd);
	t1.join();
	t2.join();
	return 0 ;
}
