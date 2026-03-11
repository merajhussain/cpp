from linkedlist import *


def test_createLinkList():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ls = "1->2->3->4->5"
    assert  ls == ll.to_String()

def test_reverseLinkedList():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)

    ls ="3->2->1"
    ll.reverse()
    assert ls == ll.to_String()

def test_swapNodesList():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.swapNodes(2,5)
    ls = "1->5->3->4->2"
    assert ls == ll.to_String()

def test_swapNodesListHead():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.swapNodes(1,5)
    ls = "5->2->3->4->1"
    assert ls == ll.to_String()

def test_addNodeAtHead():
    ll = LinkedList()
    ll.addAtHead(1)
    ll.addAtHead(2)
    ll.addAtHead(3)
    ls = "3->2->1"
    assert ls == ll.to_String()