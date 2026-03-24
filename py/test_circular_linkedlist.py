import pytest

from CircularList import CircularList
from CircularListChecker import CircularListChecker
from linkedlist import LinkedList


def test_append():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    expected = "1->2->3"
    assert expected == cl.to_string()

def test_deleteNode():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.deleteNode(3)
    expected = "1->2->4"
    assert expected == cl.to_string()

def test_deleteNodeHead():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.deleteNode(1)
    expected = "2->3->4"
    assert expected == cl.to_string()

def test_splitCircularListEvenLength():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    [l1,l2]=cl.splitList()
    expected1 = "1->2"
    expected2 = "3->4"
    assert expected1 == l1.to_string() and expected2 == l2.to_string()

def test_splitCircularListOddLength():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.append(5)
    [l1,l2]=cl.splitList()
    expected1 = "1->2->3"
    expected2 = "4->5"
    assert expected1 == l1.to_string() and expected2 == l2.to_string()

def test_JosephSurvivor():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.append(5)
    cl.append(6)
    cl.append(7)
    cl.append(8)
    eliminations = cl.joseph_survivor(4)
    survivor = "6"
    expected_eliminations = [4,8,5,2,1,3,7]
    assert survivor == cl.to_string() and eliminations == expected_eliminations

def test_isCircular():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    assert True==CircularListChecker.is_circular(cl)


def test_invalidListAssertion():
    with pytest.raises(AssertionError):
        CircularListChecker.is_circular([1,2,3])