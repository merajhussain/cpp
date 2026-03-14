from Node import Node

class CircularList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            current=self.head
            while current and current.next!=self.head:
                current=current.next
            if current:
                current.next=new_node
        new_node.next=self.head

    def __iter__(self):
        current=self.head
        while current.next != self.head:
            yield current.data
            current=current.next
        yield current.data

    def delete(self,key):
        current=self.head
        prev=None
        if key == self.head.data:
            while current.next != self.head:
                prev=current
                current=current.next


            prev = current
            current = current.next
            prev.next=current.next
            self.head=current.next
            return
        while current:
            if current.data==key:
                prev.next=current.next
                return
            else:
                prev=current
                current=current.next

    def to_string(self):
        s = "->".join(map(str,self))
        return s


