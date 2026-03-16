from Ilist import Ilist
from dlnode import dll_node


class doublyLinkedList(Ilist):

    def __init__(self):
        self.head=None

    def append(self, item):
        if self.head == None:
            self.head = dll_node(item)
        else:
            current = self.head
            while current.next!=None:
                current = current.next
            new_node = dll_node(item)
            current.next = new_node
            new_node.prev = current


    def deleteNode(self, item):
        pass

    def __len__(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count


    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def to_string(self):
        return "->".join(map(str,self))


    def prepend(self, item):
        if self.head == None:
            self.head = dll_node(item)
        else:
            new_node = dll_node(item)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node



dll = doublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

