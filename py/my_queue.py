class my_queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def __iter__(self):
        for item in self.queue:
            yield item

    def to_string(self):
        return "->".join(map(str, iter(self.queue)))

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None