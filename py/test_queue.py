from my_queue import my_queue


def test_queue_enqueue():
    queue = my_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    expected = "1->2"
    assert expected == queue.to_string()

def test_queue_dequeue():
    queue = my_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    item = queue.dequeue()
    expected = "2->3"
    assert expected == queue.to_string() and item == 1

def test_queue_size():
    queue = my_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = 3
    assert expected == queue.size()

def test_queue_peek():
    queue = my_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = 1
    assert expected == queue.peek()