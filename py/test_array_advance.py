from arrayadvance import array_advance


def test_array_advance():
    elems=[3,2,0,0,2,0,1]
    expected = False
    assert expected == array_advance(elems)

def test_array_advance1():
    elems=[3,3,1,0,2,0,1]
    expected = True
    assert expected == array_advance(elems)

def test_array_advance2():
    elems=[2,3,1,1,4]
    expected = True
    assert expected == array_advance(elems)

def test_array_advance3():
    elems=[3,2,1,0,4]
    expected = False
    assert expected == array_advance(elems)

def test_array_advance4():
    elems=[0]
    expected = True
    assert expected == array_advance(elems)

def test_array_advance5():
    elems=[0,1]
    expected = False
    assert expected == array_advance(elems)

def test_array_advance6():
    elems=[2,0,0]
    expected = True
    assert expected == array_advance(elems)

def test_array_advance7():
    elems=[1,1,0,1]
    expected = False
    assert expected == array_advance(elems)

def test_array_advance8():
    elems=[5,0,0,0,0,0]
    expected = True
    assert expected == array_advance(elems)

def test_array_advance9():
    elems=[2,1,0,0]
    expected = False
    assert expected == array_advance(elems)


