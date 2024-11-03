

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <mutex>
#include <memory>
#include <condition_variable>
#include<queue>
#include<map>

using namespace std;

class TrieNode {

public:

	TrieNode* children[26];
	bool endOfWord = false;
	char ch;
	int prefixCount;

	TrieNode(char ch) {
		for (int i = 0; i < 26; i++) {

			children[i] = nullptr;
			endOfWord = false;
			this->ch = ch;
			prefixCount = 0;
		}


	}



};

class MyTrie {

public:
	TrieNode* root;

	MyTrie() {
		root = new TrieNode('-');
	}

	void insert(string& word) {

		auto cur = root;
		for (auto ch : word) {

			int insertIndex = ch - 'a';

			if (cur->children[insertIndex] == nullptr) {

				cur->children[insertIndex] = new TrieNode(ch);

				cur = cur->children[insertIndex];

			}
			else
			{

				cur = cur->children[insertIndex];
			}
			cur->prefixCount++;
		}

		cur->endOfWord = true;
	}

	bool search(string& word) {


		auto cur = root;
		int count = 0;

		for (auto ch : word) {

			int searchIndex = ch - 'a';
			if (cur->children[searchIndex] == nullptr) {
				cur == cur->children[searchIndex];
			}
			else {
				count++;
				cur = cur->children[searchIndex];
			}
		}

		return (count == word.length()) ? true : false;
	}

	void deleteTrie(TrieNode* node) {
		if (node == nullptr) return;


		for (int i = 0; i < 26; i++) {
			if (node->children[i] != nullptr) {
				deleteTrie(node->children[i]);
			}

		}

		delete node;

	}

	int startsWithCount(string prefix) {

		auto cur = root;

		for (auto ch : prefix) {

			int searchIndex = ch - 'a';
			if (cur->children[searchIndex] != nullptr) {
				cur = cur->children[searchIndex];
			}
			else {
				return 0;
			}
		}

		return cur->prefixCount;

	}

	~MyTrie() {

		delete(root);
		root = nullptr;
	}
};

void testInsert() {

	MyTrie trie;
	string word = "meraj";
	trie.insert(word);
	if (trie.search(word)) {
		cout << "Test {testInsert} run successfully" << endl;
	}
	else {
		cout << "Test failed" << endl;
	}
}

void test1StartsWithCount() {

	MyTrie trie;
	string insert = "meraj";
	trie.insert(insert);
	string searchKey = "me";
	if (trie.startsWithCount(searchKey) == 1) {
		cout << "Test {test1StartsWithCount} executed succefully" << endl;
	}
	else {
		cout << "Test {test1StartsWithCount} failed :(" << endl;
	}
}


void test2StartsWithCount() {

	MyTrie trie;
	string insert1 = "meraj";
	string insert2 = "me";
	trie.insert(insert1);
	trie.insert(insert2);

	string searchKey = "me";
	if (trie.startsWithCount(searchKey) == 2) {
		cout << "Test {test2StartsWithCount} executed succefully" << endl;
	}
	else {
		cout << "Test {test2StartsWithCount} failed :(" << endl;
	}
}

int main() 
{


	MyTrie myTrie;

	testInsert();
	test1StartsWithCount();
	test2StartsWithCount();
	



	return 0;

}

