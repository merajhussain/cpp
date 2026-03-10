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

ll = LinkedList()
ll.addData(1)
ll.addData(2)
ll.addData(3)
ll.addData(4)
ll.addData(5)
ll.printLL()
ll.reverse()
ll.printLL()