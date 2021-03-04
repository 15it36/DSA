#include<bits/stdc++.h>
using namespace std;

class Node{
	public:
		int data;
		Node *next;

		Node(int value, Node *next)
		{
			this->data = value;
			this->next = next;
		}

};

int main(){
	Node head = Node(5, NULL);
	cout << head.data;
	return 0;
}