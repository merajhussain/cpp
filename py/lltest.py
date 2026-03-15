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

def test_mergeSortedLists():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.addData(1)
    l1.addData(7)
    l1.addData(9)

    l2.addData(3)
    l2.addData(4)
    l2.addData(6)
    l1.mergeTwoLists(l2)
    expected = "1->3->4->6->7->9"
    assert expected == l1.to_String()

def test_removeduplicates():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.removeDuplicates()
    expected = "1->2->3->4->5"
    assert expected == ll.to_String()

def test_deleteNode():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.deleteNode(3)
    expected = "1->2->4->5"
    assert expected == ll.to_String()

def test_deleteHeadNode():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.deleteNode(1)
    expected = "2->3->4->5"
    assert expected == ll.to_String()

def test_countNode():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(3)
    ll.addData(4)
    ll.addData(3)
    ll.addData(5)
    ll.addData(3)
    expected = 4

    assert expected == ll.countNodes(3)

def test_rotateList():
    ll = LinkedList()
    ll.addData(1)
    ll.addData(2)
    ll.addData(3)
    ll.addData(4)
    ll.addData(5)
    ll.rotateListAtPivot(3)
    expected = "4->5->1->2->3"
    assert expected == ll.to_String()

def test_moveTailToHead():
    ll = LinkedList()
    ll.addData(10)
    ll.addData(20)
    ll.addData(30)
    ll.addData(40)
    ll.moveTailToHead()
    expected = "40->10->20->30"
    assert expected == ll.to_String()

def test_listiterator():
    ll=LinkedList()
    ll.addData(10)
    ll.addData(20)
    ll.addData(30)
    assert  3 == len([x for x in ll])

def test_listIteratorEmptyList():

    ll = LinkedList()
    assert 0 == len([x for x in ll])



def test_addTwoList():
    l1 = LinkedList()
    l1.addData(1)
    l1.addData(2)
    l1.addData(9)

    l2 = LinkedList()
    l2.addData(9)
    l2.addData(2)
    l2.addData(9)
    l1.addList(l2)

    expected = "0->5->8->1"
    assert expected == l1.to_String()

def test_addTwoListWithDifferentPlaces():
    l1 = LinkedList()
    l1.addData(1)
    l1.addData(2)
    l1.addData(9)

    l2 = LinkedList()
    l2.addData(9)
    l2.addData(2)
    l1.addList(l2)

    expected = "0->5->9"
    assert expected == l1.to_String()

