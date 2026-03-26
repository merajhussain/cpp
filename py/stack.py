
class Stack:
    def __init__(self):
        self.items =[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items)==0:
            raise "Empty stack"
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __iter__(self):
        for item in self.items:
            yield item
    def to_string(self):
         return "|".join(map(str,self.items))
