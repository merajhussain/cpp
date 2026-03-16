from DoublyLinkedList import doublyLinkedList


def test_append( ):
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    expected = "1->2->3->4"
    assert expected == dll.to_string()

def test_prepend():
    dll = doublyLinkedList()
    dll.prepend(1)
    dll.prepend(2)
    dll.prepend(3)
    dll.prepend(4)
    expected = "4->3->2->1"
    assert expected == dll.to_string()

def test_len():
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    expected = 4
    assert expected == len(dll)