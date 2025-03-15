

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <mutex>
#include <memory>
#include <condition_variable>
#include<queue>
#include<map>
#include<list>
#include<set>
#include <iostream>
#include <thread>
#include <mutex>
using namespace std;


string longestCommonPrefix(vector<string> vec) {

	sort(vec.begin(), vec.end());

	string start = vec[0];
	string end = vec[vec.size() - 1];
	int i = 0;
	string longestPrefix;
	while (start[i] == end[i]) {
		longestPrefix += start[i];
		i++;
	}

	return longestPrefix;

}

int main() {

	vector<string>  strs = { "cat","car","catapult","caffeine"};

	cout << longestCommonPrefix(strs) << endl;

	return 0;

}