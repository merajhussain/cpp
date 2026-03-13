from CircularList import CircularList

def test_append():
    cl = CircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    expected = "1->2->3"
    assert expected == cl.to_string()