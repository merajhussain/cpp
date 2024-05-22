#include <iostream>
#include <array>
#include <vector>
#include <map>
#include <unordered_map>
#include <mutex>
#include <condition_variable>

using namespace std;

mutex mtx;
condition_variable cv;
int counter = 0;

void printOdd()
{
	while (counter < 10)
	{
		std::unique_lock<std::mutex> lk(mtx);
		 

		cv.wait(lk, []() { return (counter % 2) != 0; });
		cout << counter << endl;
		++counter;
		lk.unlock();
		cv.notify_all();
	}
	
}


void printEvn()
{
	while (counter < 10)
	{
		std::unique_lock<std::mutex> lock(mtx);
		 
		 
		cv.wait(lock, []() { return (counter % 2 == 0); });
		cout << counter << endl;
		++counter;
		lock.unlock();
		cv.notify_all();
	}

}
int main()
{
    
	thread t1(printEvn);
	thread t2(printOdd);

	t1.join();
	t2.join();
	
	 
	return 0;
}