from stack import Stack


def test_stack_push():
    stk = Stack();
    stk.push(1);
    stk.push(2);
    stk.push(3);
    expected = "1|2|3"
    assert expected == stk.to_string()

def test_stack_pop():
    stk = Stack()
    stk.push(1);
    stk.push(2);
    stk.push(3);
    stk.pop()
    expected = "1|2"
    assert expected == stk.to_string()

def test_stack_size():
    stk = Stack()
    stk.push(1);
    stk.push(2);
    stk.push(3);
    expected = 3
    assert expected == stk.size()

def test_stack_peek():
    stk = Stack()
    stk.push(1);
    stk.push(2);
    stk.push(3);
    expected = 3
    assert expected == stk.peek()