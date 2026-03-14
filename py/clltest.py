from CircularList import CircularList

def test_append():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    expected = "1->2->3"
    assert expected == cl.to_string()

def test_delete():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.delete(3)
    expected = "1->2->4"
    assert expected == cl.to_string()

def test_deleteHead():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.delete(1)
    expected = "2->3->4"
    assert expected == cl.to_string()