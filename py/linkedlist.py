from Ilist import Ilist
from Node import Node

class LinkedList(Ilist):



    def __init__(self):
        self.head=None

    def addAtHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self,data):
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
                nl.append(c1.data)
                c1 = c1.next
            else:
                nl.append(c2.data)
                c2 = c2.next
        if c1:
            while c1:
                nl.append(c1.data)
                c1 = c1.next
        if c2:
            while c2:
                nl.append(c2.data)
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

    def deleteNode(self,key):
        curr = self.head
        prev = None
        if self.head.data == key:
            self.head = curr.next
            return

        while curr:
            if curr.data == key:
                prev.next = curr.next
                return
            else:
                prev = curr
                curr = curr.next

    def rotateListAtPivot(self,pivot):

        if self.head is None:
            return

        curr = self.head
        next = None
        while curr:
            if curr.data == pivot:
                next = curr.next
                curr.next = None
                break
            curr = curr.next
        if next:
            c = next
            p = None
            while c:
                p = c
                c = c.next

            p.next = self.head
            self.head = next


    def countNodes(self,data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count

    def moveTailToHead(self):
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
            curr.next = self.head
            self.head = curr

    def addList(self,l2):
        if not self.head or not l2:
            return
        c1=self.head
        c2= l2.head
        carry =0
        sumList = LinkedList()
        while c1 and c2:

            sum = c1.data+c2.data+carry
            if sum >= 10:
                sum = sum%10
                carry = 1
            else:
                carry=0

            sumList.append(sum)
            c1 = c1.next
            c2 = c2.next
        if c1:
            while c1:
                sum = c1.data+carry
                if sum >= 10:
                    sum = sum%10
                    carry = 1
                else:
                    carry =0
                sumList.append(sum)
                c1 = c1.next
        if c2:
            while c2:
                sum = c2.data+carry
                if sum >= 10:
                    sum = sum%10
                    carry = 1
                else:
                    carry = 0
                sumList.append(sum)
                c2 = c2.next
        if carry>0:
            sumList.append(carry)
        self.head = sumList.head

    def to_string(self):
        return "->".join(map(str, self))

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def prepend(self, item):
        raise NotImplementedError




