class Node:
    def __init__(self,data):
        self.data = data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def addAtHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def addData(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def printLL(self):
        curr = self.head

        while curr:
            print(curr.data,end="")
            if curr.next:
                print("->",end="")
            curr = curr.next
        print()

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        self.head = prev

    def swapNodes(self,key1,key2):
        if key1 == key2:
            return
        c1 = self.head
        p1=None
        c2 = self.head
        p2=None
        while c1 and c1.data!=key1:
            p1=c1
            c1=c1.next
        #print(c1.data)

        while c2 and c2.data != key2:
            p2 = c2
            c2 = c2.next

        if p1:
            p1.next = c2
        else:
            self.head = c2

        if p2:
            p2.next = c1
        else:
            self.head = c1

        c1.next ,c2.next = c2.next,c1.next
        #print(c2.data)

    def mergeTwoLists(self, l2):
        c1 = self.head
        c2 = l2.head

        nl = LinkedList()
        while c1 and c2:
            if c1.data <= c2.data:
                nl.addData(c1.data)
                c1 = c1.next
            else:
                nl.addData(c2.data)
                c2 = c2.next
        if c1:
            while c1:
                nl.addData(c1.data)
                c1 = c1.next
        if c2:
            while c2:
                nl.addData(c2.data)
                c2 = c2.next

        self.head = nl.head

    def removeDuplicates(self):
        dup = dict()
        curr = self.head
        prev = None
        while curr:
            if curr.data in dup:
                prev.next = curr.next
                curr = curr.next
            else:
                dup[curr.data] = 1
                prev = curr
                curr = curr.next

    def to_String(self):
        curr = self.head
        ls=""
        while curr:
            ls += str(curr.data)
            if curr.next:
                ls +="->"
            curr = curr.next
        return ls