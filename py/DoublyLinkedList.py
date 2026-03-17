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
        if self.head == None:
            return

        if self.head.data == item:
            next_node = self.head.next
            self.head = next_node
            return

        current = self.head
        while current.data != item:
            current = current.next
        next = current.next
        prev = current.prev
        prev.next = next
        if next != None:
            next.prev = prev

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

    def add_node_after(self,key,item):
        new_node = dll_node(item)
        current = self.head
        if self.head == None:
            self.head = dll_node(item)
        else:
            while current.data != key:
                current = current.next
            next = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = next
            if next != None:
                next.prev = new_node

    def add_node_before(self,key,item):
        new_node = dll_node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.data != key:
                current = current.next
            prev = current.prev
            if prev != None:
                prev.next = new_node
                new_node.prev = prev
                new_node.next = current
                current.prev = new_node
            else:
                current.prev = new_node
                new_node.next = current
                self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
        self.head = prev

    def delete_list_node(self,node):
        if self.head == None:
            return

        if self.head  == node:
            next_node = self.head.next
            self.head = next_node

        current = self.head
        while current:
            if current == node:
                next = current.next
                prev = current.prev
                prev.next = next
                if next != None:
                    next.prev = prev
                return
            current = current.next

    def getNode(self,data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next

    def remove_duplicates(self):
        dups = dict()
        current = self.head
        while current:
            if current.data in dups:
                self.delete_list_node(current)
            else:
                dups[current.data] = 1
            current = current.next



