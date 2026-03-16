from CircularListChecker import CircularListChecker
from linkedlist import *

def test_createLinkList():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ls = "1->2->3->4->5"
    assert  ls == ll.to_string()

def test_reverseLinkedList():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ls ="3->2->1"
    ll.reverse()
    assert ls == ll.to_string()

def test_swapNodesList():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.swapNodes(2,5)
    ls = "1->5->3->4->2"
    assert ls == ll.to_string()

def test_swapNodesListHead():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.swapNodes(1,5)
    ls = "5->2->3->4->1"
    assert ls == ll.to_string()

def test_addNodeAtHead():
    ll = LinkedList()
    ll.addAtHead(1)
    ll.addAtHead(2)
    ll.addAtHead(3)
    ls = "3->2->1"
    assert ls == ll.to_string()

def test_mergeSortedLists():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append(1)
    l1.append(7)
    l1.append(9)

    l2.append(3)
    l2.append(4)
    l2.append(6)
    l1.mergeTwoLists(l2)
    expected = "1->3->4->6->7->9"
    assert expected == l1.to_string()

def test_removeduplicates():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.removeDuplicates()
    expected = "1->2->3->4->5"
    assert expected == ll.to_string()

def test_deleteNode():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.deleteNode(3)
    expected = "1->2->4->5"
    assert expected == ll.to_string()

def test_deleteHeadNode():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.deleteNode(1)
    expected = "2->3->4->5"
    assert expected == ll.to_string()

def test_countNode():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.append(4)
    ll.append(3)
    ll.append(5)
    ll.append(3)
    expected = 4

    assert expected == ll.countNodes(3)

def test_rotateList():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.rotateListAtPivot(3)
    expected = "4->5->1->2->3"
    assert expected == ll.to_string()

def test_moveTailToHead():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.moveTailToHead()
    expected = "40->10->20->30"
    assert expected == ll.to_string()

def test_listiterator():
    ll=LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert  3 == len([x for x in ll])

def test_listIteratorEmptyList():

    ll = LinkedList()
    assert 0 == len([x for x in ll])



def test_addTwoList():
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(9)

    l2 = LinkedList()
    l2.append(9)
    l2.append(2)
    l2.append(9)
    l1.addList(l2)

    expected = "0->5->8->1"
    assert expected == l1.to_string()

def test_addTwoListWithDifferentPlaces():
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(9)

    l2 = LinkedList()
    l2.append(9)
    l2.append(2)
    l1.addList(l2)

    expected = "0->5->9"
    assert expected == l1.to_string()

def test_isSingleLinkedListCircular():
    li= LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    assert False == CircularListChecker.is_circular(li)