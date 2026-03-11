class Node:
    def __init__(self,data):
        self.data = data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

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


ll = LinkedList()
ll.addData(1)
ll.addData(2)
ll.addData(3)
ll.addData(4)
ll.addData(5)
ll.printLL()
ll.reverse()
ll.printLL()
ll.swapNodes(5,4)
ll.printLL()