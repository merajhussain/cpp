

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

	TrieNode( char ch) {
		for (int i = 0; i < 26; i++) {

			children[i] = nullptr;
			endOfWord = false;
			this->ch = ch;
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
		cout << "Test run successfully" << endl;
	}
	else {
		cout << "Test failed" << endl;
	}
}

int main() {


	MyTrie myTrie;

	string word = "meraj";
	string word1 = "mer";

	testInsert();



	return 0;

}

 