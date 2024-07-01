#include <iostream>
#include <future>
#include <stdexcept>
#include<iostream>
#include <chrono>
using namespace std;

 
int task() {
    std::this_thread::sleep_for(std::chrono::seconds(10)); // Simulate a long-running task
    return 100;
}

void checkFuture(future<int> &f) {

    while (1) {



        try {
            if (f._Is_ready()) {
                cout << "Future is computed" << endl;
                cout << f.get() << endl;
                return;
          }
            else {
                cout << "waiting for future to be computed"<<endl;
            }

        }
        catch (const std::exception& e) {
            std::cerr << "Exception: " << e.what() << std::endl;
        }

    }

}



int main() {
    std::future<int> result = std::async(std::launch::async, task);

    thread t1(checkFuture, std::ref(result));


    t1.join();

   
    return 0;
}
