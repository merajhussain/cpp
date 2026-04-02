
from array_search import *
import time



def test_linear_search1():
    arr = [1,3,5,7,9,11]
    index = linear_search(arr,15)
    expected = -1
    assert index == expected


def test_linear_search2():
    arr = [1,3,5,7,9,11]
    index = linear_search(arr,5)
    expected = 2
    assert index == expected

def test_binary_search1():
    arr = [1,3,5,7,9,11]
    index = binary_search(arr,15)
    expected = -1
    assert index == expected


def test_binary_search2():
    arr = [1,3,5,7,9,11]
    index = binary_search(arr,5)
    expected = 2
    assert index == expected

def test_performace():
    arr = [x for x in range(100000000)]
    s1 = time.perf_counter()
    i1=linear_search(arr, 100000000)

    e1 = time.perf_counter()
    elapsed1 = e1 - s1
    print()
    print("Linear search elapsed time:",format(elapsed1, '.15f'))
    s2 = time.perf_counter()
    i2=binary_search(arr, 100000000)
    e2 = time.perf_counter()
    elapsed2 = e2 - s2
    print("Binary search elapsed:",format(elapsed2, '.15f'))
    assert elapsed1 > elapsed2 and i1==i2

def test_fixed_point1():
    arr = [-10, -5, 0, 3, 7]
    assert 3 == fixed_number(arr)

def test_fixed_point2():
    arr = [0, 2, 5, 8, 17]
    assert 0 == fixed_number(arr)

def test_fixed_point3():
    arr = [-10, -5, 3, 4, 7, 9]
    assert None == fixed_number(arr)