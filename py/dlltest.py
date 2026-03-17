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

def test_append_after():
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    dll.add_node_after(2,5)
    expected = "1->2->5->3->4"
    assert expected == dll.to_string()

def test_append_before():
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    dll.add_node_before(1, 6)
    dll.add_node_before(2, 5)
    print(dll.to_string())
    expected = "6->1->5->2->3->4"
    assert expected == dll.to_string()

def test_delete_node():
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.deleteNode(2)
    expected = "1->3->4->5"
    assert expected == dll.to_string()

def test_delete_head_node():
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.deleteNode(1)
    expected = "2->3->4->5"
    assert expected == dll.to_string()

def test_delete_tail_node():
    dll = doublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.deleteNode(5)
    expected = "1->2->3->4"
    assert expected == dll.to_string()


