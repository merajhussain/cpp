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

    def splitList(self):

        mid = len(self)//2
        curr = self.head
        prev = None
        l1 = CircularList()
        l2 = CircularList()
        i =0
        for val in self:
            if i<=mid:
                l1.append(val)
            else:
                l2.append(val)
            i +=1
        return [l1,l2]
        


    def to_string(self):
        s = "->".join(map(str,self))
        return s

    def __len__(self):
        current=self.head
        count=0
        while current.next != self.head:
            current=current.next
            count+=1
        return count


